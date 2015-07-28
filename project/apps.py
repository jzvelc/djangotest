from django.db.models.signals import post_migrate
from users.apps import UsersConfig as BaseUsersConfig
from .management import create_default_user


class UsersConfig(BaseUsersConfig):
    def ready(self):
        super(UsersConfig, self).ready()
        post_migrate.connect(create_default_user, sender=self)
