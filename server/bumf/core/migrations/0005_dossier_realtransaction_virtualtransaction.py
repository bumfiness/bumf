# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-07 22:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_realaccount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dossier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='A dossier may be named to remember, search and find its contents', max_length=60, null=True, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='RealTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('destination', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='incoming_transactions', to='core.RealAccount', verbose_name='Account the money moves to')),
                ('dossier', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='bank_transactions', to='core.Dossier', verbose_name='Bank transaction')),
                ('source', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='outgoing_transactions', to='core.RealAccount', verbose_name='Account the money moves away from')),
            ],
        ),
        migrations.CreateModel(
            name='VirtualTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(blank=True, max_length=1000, null=True)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('bank_transaction', models.ForeignKey(blank=True, help_text='The real-world bank transaction that describes this transaction.', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='transactions', to='core.RealTransaction', verbose_name='Bank transaction')),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='incoming_transactions', to='core.VirtualAccount', verbose_name='Virtual account the money moves to')),
                ('dossier', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='transactions', to='core.Dossier', verbose_name='Transaction')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='outgoing_transactions', to='core.VirtualAccount', verbose_name='Virtual account the money moves away from')),
            ],
        ),
    ]
