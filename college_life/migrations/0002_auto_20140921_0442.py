# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('college_life', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='major',
            name='skills',
        ),
        migrations.AddField(
            model_name='skill',
            name='major',
            field=models.ForeignKey(related_name=b'skills', default=1, to='college_life.Major'),
            preserve_default=False,
        ),
    ]
