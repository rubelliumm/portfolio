from django.apps import AppConfig


class JobappConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "jobapp"


class savedCircularConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "savedcircular"

    def ready(self):
        import jobapp.signals

        return super().ready()
