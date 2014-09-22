# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('college_life', '0014_auto_20140922_1704'),
    ]

    operations = [
        migrations.AddField(
            model_name='major',
            name='attack_description',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mob',
            name='attack_description',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='monster',
            name='attack_description',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='skill',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
    ]
