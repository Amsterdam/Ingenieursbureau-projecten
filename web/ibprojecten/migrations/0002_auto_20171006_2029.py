# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-06 18:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ibprojecten', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='Accounthouder',
            new_name='Accountant',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='Bestuurlijkopdrachtgever',
            new_name='AdministrativeClient',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='Opdrachtverantwoordelijke',
            new_name='MainContractor',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='Ambtelijkopdrachtgever',
            new_name='OfficalClient',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='Deelprojectleider',
            new_name='SubContractor',
        ),
    ]
