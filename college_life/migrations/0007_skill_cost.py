# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('college_life', '0006_auto_20140921_0456'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='cost',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
