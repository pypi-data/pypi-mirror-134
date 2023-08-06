import requests

from allauth.socialaccount import app_settings
from allauth.socialaccount.providers.oauth2.views import (
    OAuth2Adapter,
    OAuth2CallbackView,
    OAuth2LoginView,
)
from .provider import JetbrainsHubProvider


class JetbrainsHubAuth2Adapter(OAuth2Adapter):
    provider_id = JetbrainsHubProvider.id

    settings = app_settings.PROVIDERS.get(provider_id, {})
    server = settings.get("SERVER")

    # remove a trailing slash from the server.
    if server[-1] == '/':
        server = server[:-1]

    authorize_url = f'{server}/api/rest/oauth2/auth'
    access_token_url = f'{server}/api/rest/oauth2/token'
    profile_url = f'{server}/api/rest/oauth2/userinfo'

    def complete_login(self, request, app, token, **kwargs):
        headers = {'Authorization': 'Bearer {0}'.format(token.token)}
        resp = requests.get(self.profile_url, headers=headers)
        extra_data = resp.json()

        return self.get_provider().sociallogin_from_response(
            request,
            extra_data,
        )


oauth2_login = OAuth2LoginView.adapter_view(JetbrainsHubAuth2Adapter)
oauth2_callback = OAuth2CallbackView.adapter_view(JetbrainsHubAuth2Adapter)
