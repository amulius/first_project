# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('college_life', '0002_auto_20140921_0442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='major',
            field=models.ForeignKey(related_name=b'skills', blank=True, to='college_life.Major', null=True),
        ),
    ]
