"""
Django settings for djangoProject project.

Generated by 'django-admin startproject' using Django 3.2.22.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
import time
# Build paths inside the project like this: BASE_DIR / 'subdir'.

BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-(=^k+_swcx(q*e^0w6wqlip-5x+#-35a@y^qc4@-p_o)g9f*th'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*','10.50.90.13']

# Application definition



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',  # 管理静态文件
    'djangoProject',





]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'djangoProject.urls'

LOG_PATH = BASE_DIR / "logs"

if not os.path.exists(LOG_PATH):
    os.mkdir(LOG_PATH)
#
LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        # 日志格式

        # "standard": {"format": "%(asctime)s  %(levelname)-5s  %(filename)-10s.%(funcName)-20s   [%(lineno)-4d] :%(message)-s"},
'standard': {'format': '%(asctime)s  [%(name)s:%(lineno)d] '
                               '[%(module)s:%(funcName)s] [%(levelname)s]- %(message)s'},

        "simple": {"format": "%(levelname)s %(message)s"},  # 简单格式
    },
    # 过滤
    "filters": {},
    # 定义具体处理日志的方式
    "handlers": {
        # 默认记录所有日志
        "default": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": LOG_PATH / f'system-{time.strftime("%Y-%m-%d")}.log',
            "maxBytes": 1024 * 1024 * 5,  # 文件大小
            "backupCount": 15,  # 备份数
            "formatter": "standard",  # 输出格式
            "encoding": "utf-8",  # 设置默认编码，否则打印出来汉字乱码
            "delay":True,
        },
        # 输出错误日志
        "error": {
            "level": "ERROR",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": LOG_PATH / f'error-{time.strftime("%Y-%m-%d")}.log',
            "maxBytes": 1024 * 1024 * 5,  # 文件大小 5mb
            "backupCount": 5,  # 备份数
            "formatter": "standard",  # 输出格式
            "encoding": "utf-8",  # 设置默认编码
        },
        # 控制台输出
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "standard",
        },
    },
    # 配置用哪几种 handlers 来处理日志
    "loggers": {
        # 类型 为 django 处理所有类型的日志， 默认调用
        "django": {
            "level": "DEBUG",
            "handlers": ["default", "console"],
            "propagate": False,
        },
        # log 调用时需要当作参数传入
        "log": {
            "level": "INFO",
            "handlers": ["error", "console", "default"],
            "propagate": True,
        },
    },
}




TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
#
# SESSION_ENGINE='django.contrib.sessions.backends.db'

WSGI_APPLICATION = 'djangoProject.wsgi.application'
# 允许所有资源访问
CORS_ORIGIN_ALLOW_ALL = True

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

#测试环境
ENV = "http://10.2.145.216:9090"
#开发环境
# ENV = ''
os.environ["ENV"] = ENV

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.oracle',
        'USER': 'gf_otc',
        'PASSWORD': 'otc1qazXSW@',
        'HOST': '10.62.146.18',
        'PORT': '1521',
        'NAME': 'jgjtest'
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/
# 修改成中文界面
LANGUAGE_CODE = 'zh-hans'
# 时区
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS=[
    os.path.join(BASE_DIR,"static")
]
