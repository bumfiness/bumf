# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-06 19:15
from __future__ import unicode_literals

import bumf.core.models.auth
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='Give your project a name if you have multiple projects!', max_length=60, null=True, verbose_name='Name')),
                ('scope', models.CharField(choices=[('private', 'private'), ('business', 'business')], default='private', max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='nick',
            field=models.CharField(help_text='Please use only characters in the latin alphabet, plus numbers and _-.', max_length=60, unique=True, validators=[bumf.core.models.auth.nick_validator], verbose_name='Nickname'),
        ),
        migrations.AddField(
            model_name='project',
            name='user',
            field=models.ForeignKey(help_text="The project's owner", on_delete=django.db.models.deletion.PROTECT, related_name='projects', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]
