import os

import dj_database_url

from base import *

# https://devcenter.heroku.com/articles/django#django-settings

# Parse database configuration from $DATABASE_URL
DATABASES['default'] = dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# To set environment variables see config_heroku_sample.sh in root of the project
TWITTER_CONSUMER_KEY = os.environ['TWITTER_CONSUMER_KEY']
TWITTER_CONSUMER_SECRET = os.environ['TWITTER_CONSUMER_SECRET']
GITHUB_APP_ID = os.environ['GITHUB_APP_ID']
GITHUB_API_SECRET = os.environ['GITHUB_API_SECRET']
