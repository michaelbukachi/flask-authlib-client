import requests
from authlib.oauth2.rfc6749 import TokenMixin, time
from authlib.oauth2.rfc6750 import BearerTokenValidator
from flask import current_app


class RemoteTokenValidator(BearerTokenValidator):

    def __init__(self, token_cls, realm=None):
        super().__init__(realm)
        self.token_cls = token_cls

    def authenticate_token(self, token_string):
        url = current_app.config['RESOURCE_SERVER_INTROSPECTION_URL']
        credentials = current_app.config['RESOURCE_SERVER_INTROSPECTION_CREDENTIALS']
        res = requests.post(url, data={'token': token_string}, auth=credentials)
        if res.ok:
            return self.token_cls(res.json())

        return None

    def request_invalid(self, request):
        return False

    def token_revoked(self, token):
        return token.is_revoked()


class RemoteToken(TokenMixin):

    def __init__(self, token):
        self.token = token

    def get_client_id(self):
        return self.token.get('client_id', None)

    def get_scope(self):
        return self.token.get('scope', None)

    def get_expires_in(self):
        return self.token.get('exp', 0)

    def get_expires_at(self):
        expires_at = self.get_expires_in() + self.token.get('iat', 0)
        if expires_at == 0:
            expires_at = time.time() + 3600  # Expires in an hour
        return expires_at

    def is_revoked(self):
        return not self.token.get('active', False)
