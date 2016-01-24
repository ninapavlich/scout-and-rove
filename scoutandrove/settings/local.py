from scoutandrove.settings.base import *

#==============================================================================
# Generic Django project settings
#==============================================================================


DEBUG = True
TEMPLATE_DEBUG = DEBUG
ALLOWED_HOSTS = ['*']
HTML_MINIFY = True

#==============================================================================
# LOCAL DATBASE
#==============================================================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(VAR_ROOT, 'scoutandrove'),
    },
}