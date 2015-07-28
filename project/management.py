'''
Creates the default Site object.
'''

from django.apps import apps
from django.conf import settings
from django.db import DEFAULT_DB_ALIAS, router


def create_default_user(app_config, verbosity=2, interactive=True, using=DEFAULT_DB_ALIAS, **kwargs):
    try:
        User = apps.get_model('dlabs_users', 'User')
    except LookupError:
        return

    if not router.allow_migrate(using, User):
        return

    if not User.objects.using(using).exists():
        if hasattr(settings, 'ADMINS'):
            for admin in settings.ADMINS:
                if verbosity >= 2:
                    print('Creating user %s' % admin[1])
                name = admin[0].split(' ')
                if len(name) >= 2:
                    User.objects.create_superuser(
                        email=admin[1],
                        first_name=name[0],
                        last_name=name[1],
                        password='admin'
                    ).save(using=using)
                else:
                    User.objects.create_superuser(
                        email=admin[1],
                        password='admin'
                    ).save(using=using)
