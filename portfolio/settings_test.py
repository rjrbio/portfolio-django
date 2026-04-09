"""
Settings para el entorno de pruebas.
Usa SQLite en memoria para evitar dependencia de PostgreSQL en CI/test local.
"""
from .settings import *  # noqa: F401, F403

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

# Mantiene los rates para que los throttles no fallen, pero usa DummyCache
# para que nunca acumulen entre tests.
REST_FRAMEWORK['DEFAULT_THROTTLE_CLASSES'] = [  # noqa: F405
    'rest_framework.throttling.AnonRateThrottle',
    'rest_framework.throttling.UserRateThrottle',
]
REST_FRAMEWORK['DEFAULT_THROTTLE_RATES'] = {  # noqa: F405
    'anon': '10000/hour',
    'user': '10000/hour',
    'contact': '10000/hour',
    'agent': '10000/hour',
}

# Caché dummy para que los throttles personalizados no persistan entre tests
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

# Silencia warnings de password hashers lentos en tests
PASSWORD_HASHERS = ['django.contrib.auth.hashers.MD5PasswordHasher']
