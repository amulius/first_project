# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('college_life', '0011_monster_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='hp_max',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='character',
            name='mp_max',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
