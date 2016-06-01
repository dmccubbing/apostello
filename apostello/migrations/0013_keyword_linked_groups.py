# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-01 10:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apostello', '0012_keyword_disable_all_replies'),
    ]

    operations = [
        migrations.AddField(
            model_name='keyword',
            name='linked_groups',
            field=models.ManyToManyField(blank=True, help_text='Contacts that match this keyword will be added to the selected groups.', to='apostello.RecipientGroup'),
        ),
    ]
