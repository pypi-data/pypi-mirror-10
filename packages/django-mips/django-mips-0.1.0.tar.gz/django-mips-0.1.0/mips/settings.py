"""Settings file """


import dbsettings_default as dbsettings

# for production use!
try:
    import dbsettings_production as dbsettings
except:
    pass

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = dbsettings.SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
ALLOWED_HOSTS = dbsettings.ALLOWED_HOSTS


INSTALLED_APPS = [
    # 'django.contrib.admin',
    # 'django.contrib.auth',
    # 'django.contrib.contenttypes',
    # 'django.contrib.sessions',
    # 'django.contrib.messages',
]

MIDDLEWARE_CLASSES = (
    # 'django.contrib.sessions.middleware.SessionMiddleware',
    # 'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    # 'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'django.contrib.messages.middleware.MessageMiddleware',
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': dbsettings.DBNAME,
        'USER': dbsettings.USER,
        'PASSWORD': dbsettings.PASSWORD,
        'HOST': dbsettings.HOST
    }
}
