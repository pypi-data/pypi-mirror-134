from setuptools import setup, find_packages

setup(
    name = "django-allauth-jetbrains-hub",
    version = "0.0.1",
    author = "Gary Kramlich",
    author_email = "grim@reaperworld.com",
    description = "Jetbrains Hub OAuth2 provider for django-allauth",
    url = "https://keep.imfreedom.org/grim/django-allauth-jetbrains-hub",
    packages=find_packages(),
    install_requires=['django-allauth>=0.34.0'],
    classifiers = [
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Framework :: Django',
    ],
)
