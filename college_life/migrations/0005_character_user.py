# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('college_life', '0004_auto_20140921_0452'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='user',
            field=models.ForeignKey(related_name=b'characters', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
