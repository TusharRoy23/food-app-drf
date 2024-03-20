import os

from celery import Celery
from django.apps import AppConfig, apps
from django.conf import settings

"""
https://docs.celeryq.dev/en/latest/django/first-steps-with-django.html
"""

if not settings.configured:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.base")

# celery config
app = Celery("backend")
app.config_from_object("django.conf:settings", namespace="CELERY")


class CeleryConfig(AppConfig):
    name = "backend.taskapp"
    verbose_name = "Celery Configuration"

    def ready(self):
        installed_apps = [app_config.name for app_config in apps.get_app_configs()]
        app.autodiscover_tasks(lambda: installed_apps, force=True)


@app.task(bind=True)
def debug_task(self):
    print("Request: {0!r}".format(self.request))
