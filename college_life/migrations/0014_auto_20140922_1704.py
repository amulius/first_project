# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('college_life', '0013_character_xp_next'),
    ]

    operations = [
        migrations.AddField(
            model_name='major',
            name='image',
            field=models.ImageField(null=True, upload_to=b'major_images', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mob',
            name='image',
            field=models.ImageField(null=True, upload_to=b'monster_images', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='monster',
            name='image',
            field=models.ImageField(null=True, upload_to=b'monster_images', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='zone',
            name='image',
            field=models.ImageField(null=True, upload_to=b'zone_images', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='character',
            name='level',
            field=models.IntegerField(default=0),
        ),
    ]
