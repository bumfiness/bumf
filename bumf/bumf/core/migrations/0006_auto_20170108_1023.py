# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-08 10:23
from __future__ import unicode_literals

import bumf.core.models.account
from django.db import migrations, models
import django.db.models.deletion
import functools


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_dossier_realtransaction_virtualtransaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='default_budget_account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='core.VirtualAccount', validators=[functools.partial(bumf.core.models.account.validate_variant, *('budget',), **{})]),
        ),
        migrations.AddField(
            model_name='project',
            name='default_expense_account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='core.VirtualAccount', validators=[functools.partial(bumf.core.models.account.validate_variant, *('expense',), **{})]),
        ),
        migrations.AddField(
            model_name='project',
            name='default_income_account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='core.VirtualAccount', validators=[functools.partial(bumf.core.models.account.validate_variant, *('income',), **{})]),
        ),
    ]
