# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('college_life', '0003_auto_20140921_0445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='major',
            name='agl_multiplier',
            field=models.FloatField(default=0),
        ),
    ]
