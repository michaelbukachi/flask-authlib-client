from authlib.integrations.flask_oauth2 import ResourceProtector

from flask_authlib_client.extras import RemoteToken, RemoteTokenValidator


class AuthClient(object):

    def __init__(self, app=None, oauth=None, token_class=RemoteToken):
        """
        Constructor for flask_authlib_client.AuthClient

        :param app: Flask application
        """
        self._require_auth = None

        if app is not None:
            self.init_app(app, oauth, token_class)

    def init_app(self, app, oauth, token_class):
        """
        Configure AuthClient for Flask application

        Available configuration options:
          RESOURCE_SERVER_INTROSPECTION_URL
          RESOURCE_SERVER_INTROSPECTION_CREDENTIALS
        :param app: Flask application
        :param oauth: Oauth instance
        :param token_class: a token class which inherits from TokenMixin
        """
        require_oauth = ResourceProtector()
        require_oauth.register_token_validator(RemoteTokenValidator(token_class))
        self._require_auth = require_oauth

    @property
    def require_oauth(self):
        return self._require_auth
