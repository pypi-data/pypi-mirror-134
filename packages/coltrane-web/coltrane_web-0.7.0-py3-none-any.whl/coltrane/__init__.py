import logging
from os import getenv
from pathlib import Path
from typing import Any, Dict, List, Optional

from django.conf import settings
from django.core.handlers.wsgi import WSGIHandler
from django.urls import include, path

from dotenv import load_dotenv

from coltrane.config.settings import DEFAULT_COLTRANE_SETTINGS

from .utils import dict_merge


logger = logging.getLogger(__name__)

__all__ = [
    "initialize",
]


urlpatterns = [
    path("", include("coltrane.urls")),
]

DEFAULT_CACHES_SETTINGS = {
    "default": {
        "BACKEND": "django.core.cache.backends.dummy.DummyCache",
    }
}

DEFAULT_MIDDLEWARE_SETTINGS = [
    "django.middleware.security.SecurityMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

DEFAULT_TEMPLATES_SETTINGS = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
        "DIRS": [
            "templates",
        ],
    },
]


def _get_base_dir(base_dir: Optional[Path]) -> Path:
    if base_dir is None:
        base_dir = Path(".")
    elif isinstance(base_dir, str):
        base_dir = Path(base_dir)

    return base_dir


def _merge_installed_apps(django_settings: Dict[str, Any]) -> List[str]:
    """
    Gets the installed apps from the passed-in settings and adds `coltrane` to it.
    """

    installed_apps = list(django_settings.get("INSTALLED_APPS", []))
    installed_apps.append("coltrane")

    return installed_apps


def _merge_settings(base_dir: Path, django_settings: Dict[str, Any]) -> Dict[str, Any]:
    """
    Merges the passed-in settings into the default `coltrane` settings. Passed-in settings will override the defaults.
    """

    default_settings = {
        "BASE_DIR": base_dir,
        "ROOT_URLCONF": __name__,
        "DEBUG": getenv("DEBUG", "True") == "True",
        "SECRET_KEY": getenv("SECRET_KEY"),
        "INSTALLED_APPS": _merge_installed_apps(django_settings),
        "CACHES": DEFAULT_CACHES_SETTINGS,
        "MIDDLWARE": DEFAULT_MIDDLEWARE_SETTINGS,
        "TEMPLATES": DEFAULT_TEMPLATES_SETTINGS,
        "COLTRANE": DEFAULT_COLTRANE_SETTINGS,
    }

    django_settings = dict_merge(
        default_settings, django_settings, destination_overrides_source=True
    )
    logger.debug(f"Merged settings: {django_settings}")

    return django_settings


def _configure_settings(django_settings: Dict[str, Any]) -> None:
    """
    Configures the settings in Django.
    """

    settings.configure(**django_settings)


def initialize(
    base_dir: Optional[Path] = None,
    **django_settings: Dict[str, Any],
) -> WSGIHandler:
    """
    Initializes the Django static site.
    """

    base_dir = _get_base_dir(base_dir)

    load_dotenv(base_dir / ".env")

    django_settings = _merge_settings(base_dir, django_settings)
    _configure_settings(django_settings)

    return WSGIHandler()
