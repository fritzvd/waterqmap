from settings import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', 
        'NAME': 'test.db',               
    }
}
ADMIN_MEDIA_PREFIX = '/static/admin/'
