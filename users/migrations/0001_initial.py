# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import sorl.thumbnail.fields
import users.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, blank=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', default=False, help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('username', models.EmailField(max_length=254, unique=True, editable=False, verbose_name='Username')),
                ('email', models.EmailField(verbose_name='Email address', db_index=True, max_length=254, unique=True, help_text='Required. Email must be unique since it identifies user.')),
                ('avatar_width', models.PositiveIntegerField(null=True, blank=True)),
                ('avatar_height', models.PositiveIntegerField(null=True, blank=True)),
                ('avatar', sorl.thumbnail.fields.ImageField(null=True, validators=[users.models.validate_avatar], upload_to=users.models.generate_avatar_filename, blank=True, verbose_name='Avatar')),
                ('first_name', models.CharField(null=True, max_length=30, blank=True, verbose_name='First name')),
                ('last_name', models.CharField(null=True, max_length=30, blank=True, verbose_name='Last name')),
                ('birthday', models.DateField(null=True, blank=True, verbose_name='Birthday')),
                ('gender', models.CharField(max_length=1, default='M', choices=[('M', 'Male'), ('F', 'Female')])),
                ('is_staff', models.BooleanField(verbose_name='Staff status', default=False, help_text='Designates whether the user can log into this admin site.')),
                ('is_active', models.BooleanField(verbose_name='Active', default=True, help_text='Designates whether this user should be treated as active. Deselect this instead of deleting accounts.')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Date joined')),
                ('groups', models.ManyToManyField(to='auth.Group', blank=True, related_query_name='user', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', verbose_name='groups')),
            ],
            options={
                'swappable': 'AUTH_USER_MODEL',
                'verbose_name_plural': 'users',
                'verbose_name': 'user',
            },
        ),
        migrations.CreateModel(
            name='AccessToken',
            fields=[
                ('key', models.CharField(serialize=False, primary_key=True, max_length=40)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('expiration', models.DateTimeField()),
                ('user', models.ForeignKey(related_name='access_token', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'access_tokens',
                'verbose_name': 'access_token',
            },
        ),
        migrations.CreateModel(
            name='RefreshToken',
            fields=[
                ('key', models.CharField(serialize=False, primary_key=True, max_length=40)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('expiration', models.DateTimeField()),
                ('access_token', models.ForeignKey(related_name='refresh_token', to='dlabs_users.AccessToken')),
            ],
            options={
                'verbose_name_plural': 'refresh_tokens',
                'verbose_name': 'refresh_token',
            },
        ),
        migrations.CreateModel(
            name='RememberMeToken',
            fields=[
                ('key', models.CharField(serialize=False, primary_key=True, max_length=40)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('expiration', models.DateTimeField()),
                ('user', models.ForeignKey(related_name='remember_me_token', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'remember_me_tokens',
                'verbose_name': 'remember_me_token',
            },
        ),
        migrations.CreateModel(
            name='WindsurferProfile',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('experience', models.CharField(max_length=1, default='I', choices=[('B', 'Beginner'), ('I', 'Intermediate'), ('A', 'Advanced')])),
                ('board_volume', models.PositiveIntegerField()),
                ('board_width', models.PositiveIntegerField()),
                ('board_legth', models.PositiveIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='profile',
            field=models.ForeignKey(to='dlabs_users.WindsurferProfile'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(to='auth.Permission', blank=True, related_query_name='user', help_text='Specific permissions for this user.', related_name='user_set', verbose_name='user permissions'),
        ),
    ]
