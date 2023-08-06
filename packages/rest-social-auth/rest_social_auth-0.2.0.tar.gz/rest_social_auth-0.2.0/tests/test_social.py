import json
import logging
try:
    from urlparse import parse_qsl, urlparse
except ImportError:
    # python 3
    from urllib.parse import parse_qsl, urlparse

from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model
from django.test.utils import override_settings
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from httpretty import HTTPretty
from social.utils import module_member
from social.backends.utils import load_backends
from social.tests.backends.test_facebook import FacebookOAuth2Test

from rest_social_auth.views import load_strategy

l = logging.getLogger(__name__)


# don't run third party tests
delattr(FacebookOAuth2Test, 'test_login')
delattr(FacebookOAuth2Test, 'test_partial_pipeline')


class BaseFacebookAPITestCase(FacebookOAuth2Test):

    def setUp(self):
        HTTPretty.enable()
        Backend = module_member(self.backend_path)
        self.strategy = load_strategy()
        self.backend = Backend(self.strategy, redirect_uri=self.complete_url)
        self.name = self.backend.name.upper().replace('-', '_')
        self.complete_url = self.strategy.build_absolute_uri(
            self.raw_complete_url.format(self.backend.name)
        )
        backends = (self.backend_path, )
        load_backends(backends, force_load=True)

        user_data_body = json.loads(self.user_data_body)
        self.email = 'example@mail.com'
        user_data_body['email'] = self.email
        self.user_data_body = json.dumps(user_data_body)

        start_url = self.backend.start().url
        self.auth_handlers(start_url)

    def tearDown(self):
        HTTPretty.disable()
        HTTPretty.reset()
        self.backend = None
        self.strategy = None
        self.name = None
        self.complete_url = None


class TestSocialAuth(APITestCase, BaseFacebookAPITestCase):

    def test_login_social_session(self):
        resp = self.client.post(reverse('login_social_session'),
            data={'provider': 'facebook', 'code': '3D52VoM1uiw94a1ETnGvYlCw'})
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data['email'], self.email)
        # check cookies are set
        self.assertTrue('sessionid' in resp.cookies)
        # check user is created
        self.assertTrue(
            get_user_model().objects.filter(email=self.email).exists())

    def test_login_social_token_user(self):
        resp = self.client.post(reverse('login_social_token_user'),
            data={'provider': 'facebook', 'code': '3D52VoM1uiw94a1ETnGvYlCw'})
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data['email'], self.email)
        # check token exists
        token = Token.objects.get(key=resp.data['token'])
        # check user is created
        self.assertEqual(token.user.email, self.email)

    def test_login_social_token_only(self):
        resp = self.client.post(reverse('login_social_token'),
            data={'provider': 'facebook', 'code': '3D52VoM1uiw94a1ETnGvYlCw'})
        self.assertEqual(resp.status_code, 200)
        # check token exists
        token = Token.objects.get(key=resp.data['token'])
        # check user is created
        self.assertEqual(token.user.email, self.email)

    def test_login_social_http_origin(self):
        resp = self.client.post(reverse('login_social_session'),
            data={'provider': 'facebook', 'code': '3D52VoM1uiw94a1ETnGvYlCw'},
            HTTP_ORIGIN="http://frontend.com")
        self.assertEqual(resp.status_code, 200)
        url_params = dict(parse_qsl(urlparse(HTTPretty.latest_requests[0].path).query))
        self.assertEqual(url_params['redirect_uri'], "http://frontend.com/")

    @override_settings(REST_SOCIAL_OAUTH_ABSOLUTE_REDIRECT_URI='http://myproject.com/')
    def test_login_absolute_redirect(self):
        resp = self.client.post(reverse('login_social_session'),
            data={'provider': 'facebook', 'code': '3D52VoM1uiw94a1ETnGvYlCw'})
        self.assertEqual(resp.status_code, 200)
        url_params = dict(parse_qsl(urlparse(HTTPretty.latest_requests[0].path).query))
        self.assertEqual('http://myproject.com/', url_params['redirect_uri'])

    @override_settings(REST_SOCIAL_OAUTH_ABSOLUTE_REDIRECT_URI='http://myproject.com/')
    def test_login_manual_redirect(self):
        resp = self.client.post(reverse('login_social_session'),
            data={'provider': 'facebook', 'code': '3D52VoM1uiw94a1ETnGvYlCw',
                'redirect_uri': 'http://manualdomain.com/'})
        self.assertEqual(resp.status_code, 200)
        url_params = dict(parse_qsl(urlparse(HTTPretty.latest_requests[0].path).query))
        self.assertEqual('http://manualdomain.com/', url_params['redirect_uri'])


class TestSocialAuthError(APITestCase, BaseFacebookAPITestCase):
    access_token_status = 400

    def test_login_oauth_provider_error(self):
        resp = self.client.post(reverse('login_social_session'),
            data={'provider': 'facebook', 'code': '3D52VoM1uiw94a1ETnGvYlCw'})
        self.assertEqual(resp.status_code, 400)


class TestSocialHTTPError(APITestCase, BaseFacebookAPITestCase):
    access_token_status = 401

    def test_login_oauth_provider_http_error(self):
        resp = self.client.post(reverse('login_social_session'),
            data={'provider': 'facebook', 'code': '3D52VoM1uiw94a1ETnGvYlCw'})
        self.assertEqual(resp.status_code, 400)
