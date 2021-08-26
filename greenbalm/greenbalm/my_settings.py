from greenbalm.greenbalm.settings import SECRET_KEY


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'studymanage_db',
        'USER': 'root',
        'PASSWORD': 'green',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}

SECRET_KEY = 'django-insecure-c%f8&zc*__p0r5(zbz8lm@kka-0m1y-bm@2q48nz@mrlmd1(x)'