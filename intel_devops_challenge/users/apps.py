from django.apps import AppConfig


class UsersAppConfig(AppConfig):

    name = "intel_devops_challenge.users"
    verbose_name = "Users"

    def ready(self):
        try:
            import users.signals  # noqa F401
        except ImportError:
            pass
