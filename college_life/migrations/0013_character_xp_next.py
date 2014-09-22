# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('college_life', '0012_auto_20140922_0126'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='xp_next',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
