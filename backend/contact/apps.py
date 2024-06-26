from django.apps import AppConfig


class ContactConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "backend.contact"

    def ready(self):
        import backend.contact.signals  # noqa
