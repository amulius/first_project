# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('college_life', '0008_auto_20140921_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monster',
            name='basic_attack',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
    ]
