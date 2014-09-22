# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('college_life', '0005_character_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='hp',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='character',
            name='mp',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mob',
            name='hp',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
