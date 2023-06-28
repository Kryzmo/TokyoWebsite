from django.apps import AppConfig

class AppManagmentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_managment'
    def ready(self):
        # Implicitly connect signal handlers decorated with @receiver.
        import app_managment.signals