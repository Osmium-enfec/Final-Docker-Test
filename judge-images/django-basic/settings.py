from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
SECRET_KEY = 'dummy'
DEBUG = False
ALLOWED_HOSTS = ['*']
INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'app',
]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}
ROOT_URLCONF = 'urls'
MIDDLEWARE = []
USE_TZ = True
