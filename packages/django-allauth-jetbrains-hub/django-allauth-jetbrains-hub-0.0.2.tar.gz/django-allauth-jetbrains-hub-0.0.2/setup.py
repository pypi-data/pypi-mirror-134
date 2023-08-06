from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as fp:
    long_description = fp.read()

setup(
    name = 'django-allauth-jetbrains-hub',
    version = '0.0.2',
    author = 'Gary Kramlich',
    author_email = 'grim@reaperworld.com',
    description = 'Jetbrains Hub OAuth2 provider for django-allauth',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://keep.imfreedom.org/grim/django-allauth-jetbrains-hub',
    packages=find_packages(),
    install_requires=['django-allauth>=0.34.0'],
    classifiers = [
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Framework :: Django',
    ],
)
