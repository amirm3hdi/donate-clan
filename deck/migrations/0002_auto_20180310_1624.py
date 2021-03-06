# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-10 16:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('deck', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='deck',
            options={'verbose_name': 'Deck', 'verbose_name_plural': 'Decks'},
        ),
        migrations.RenameField(
            model_name='deck',
            old_name='type',
            new_name='kind',
        ),
        migrations.RemoveField(
            model_name='deck',
            name='date_created',
        ),
        migrations.AddField(
            model_name='deck',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
