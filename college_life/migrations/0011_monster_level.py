# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('college_life', '0010_auto_20140921_1710'),
    ]

    operations = [
        migrations.AddField(
            model_name='monster',
            name='level',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
