import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     },
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME': 'test_db',

        'USER': 'root',

        'PASSWORD': 'root',

        'HOST': 'db',

        'PORT': '5432',
    }
}

DEBUG = True
# Dev only Key 
SECRET_KEY = '#*z&7_qe2+#q8$!%=pyl)7x!td=epwso@p5km&pjin6te&@a(6'
