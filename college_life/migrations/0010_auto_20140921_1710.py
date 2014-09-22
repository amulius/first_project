# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('college_life', '0009_auto_20140921_1659'),
    ]

    operations = [
        migrations.RenameField(
            model_name='monster',
            old_name='xp',
            new_name='xp_drop',
        ),
        migrations.AddField(
            model_name='monster',
            name='gp_drop',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
