
# local settings

DEBUG = True

ADMINS = (
  # ('Your Name', 'your_email@example.com'),
)

ALLOWED_HOSTS = ['localhost', 'peer']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',      # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'peer.db',                     # Or path to database file if using sqlite3.
    }
}

TIME_ZONE = 'Europe/Madrid'

RECAPTCHA_PUBLIC_KEY = ''
RECAPTCHA_PRIVATE_KEY = ''

SAML_ENABLED = False
SAML_CONFIG = {}
REMOTE_USER_ENABLED = False
