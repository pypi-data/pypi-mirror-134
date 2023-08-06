# django-allauth-jetbrains-hub

Jetbrains Hub OAuth2 provider for django-allauth

## Installation

### Requirements

* django-allauth (https://github.com/pennersr/django-allauth)

### Python Package

```
pip install django-allauth-jetbrains-hub
```

### settings.py

The server value in the path request must be set to point to your Jetbrains
hub instance and include the full path to it. For example, if your instance
is at https://example.com/ but you get redirected to https://example.com/hub/
you should set server to https://example.com/hub/.

```
INSTALLED_APPS = (
    ...
    # The following apps are required:
    'django.contrib.auth',
    'django.contrib.sites',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
     ...
     # Add allauth_microsoft to installed_apps
     'allauth_jetbrains_hub'
     ...
)

SOCIALACCOUNT_PROVIDERS = {
    'jetbrains-hub': {
        'SERVER': 'https://example.com/hub/',
    }
}

```
## Post-Installation

### Create service in your hub instance

* Create a service in your hub instance as documented [here](https://www.jetbrains.com/help/hub/add-service.html).
* Open the service in HUB.
* Set the Redirect URI to https://example.com/accounts/jetbrains-hub/login/callback/.
* Copy your Application ID and click change secret to get a new secret.
* Enter the Application ID and Secret into the Django Admin interface.

## Contributors

* Gary Kramlich <grim@reaperworld.com>

Forked from [github.com/schaenzer/django-allauth-microsoft](https://github.com/schaenzer/django-allauth-microsoft).

## License
[MIT License](LICENSE)

