"""
Purpose: Django project configuration (apps, DB, keys, static files)
"""
import os
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
load_dotenv(os.path.join(BASE_DIR, ".env"))

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "replace-me")
DEBUG = True
ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "corsheaders",
    "roads",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

CORS_ALLOW_ALL_ORIGINS = True

ROOT_URLCONF = "saferouteai.urls"
WSGI_APPLICATION = "saferouteai.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.getenv("MYSQL_DB", "saferouteai_db"),
        "USER": os.getenv("MYSQL_USER", "your_db_user"),
        "PASSWORD": os.getenv("MYSQL_PASSWORD", "your_db_password"),
        "HOST": os.getenv("MYSQL_HOST", "localhost"),
        "PORT": os.getenv("MYSQL_PORT", "3306"),
        "OPTIONS": {
            "init_command": "SET sql_mode='STRICT_TRANS_TABLES'",
        }
    }
}

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "roads" / "static"]
ORS_API_KEY = os.getenv("ORS_API_KEY")
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")
