from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider


class JetbrainsHubAccount(ProviderAccount):
    def to_str(self):
        dflt = super(JetbrainsHubAccount, self).to_str()

        return self.account.extra_data.get('name', dflt)


class JetbrainsHubProvider(OAuth2Provider):
    id = 'jetbrains-hub'
    name = 'Jetbrains Hub'
    account_class = JetbrainsHubAccount

    def get_scope(self, request):
        scope = set(super(JetbrainsHubProvider, self).get_scope(request))
        scope.add('openid')
        return list(scope)

    def get_default_scope(self):
        return ['openid']

    def extract_uid(self, data):
        return str(data['sub'])

    def extract_common_fields(self, data):
        first_name = data.get('name')
        last_name = ''
        if ' ' in first_name:
            first_name, last_name = first_name.split(' ', 1)

        return dict(
            email=data.get('email'),
            first_name=first_name,
            last_name=last_name,
            username=data.get('email'),
        )


provider_classes = [JetbrainsHubProvider]
