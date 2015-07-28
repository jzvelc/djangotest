# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dlabs_users', '0003_auto_20150728_1109'),
    ]

    operations = [
        migrations.RenameField(
            model_name='windsurfprofile',
            old_name='board_legth',
            new_name='board_length',
        ),
    ]
