# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dlabs_users', '0002_auto_20150728_1053'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='WindsurferProfile',
            new_name='WindsurfProfile',
        ),
        migrations.AlterField(
            model_name='user',
            name='profile',
            field=models.ForeignKey(related_name='user', to='dlabs_users.WindsurfProfile', null=True, blank=True),
        ),
    ]
