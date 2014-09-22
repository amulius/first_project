# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('college_life', '0007_skill_cost'),
    ]

    operations = [
        migrations.CreateModel(
            name='Monster',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=120)),
                ('xp', models.IntegerField(default=0)),
                ('hp', models.IntegerField(default=0)),
                ('str', models.IntegerField(default=0)),
                ('int', models.IntegerField(default=0)),
                ('agl', models.IntegerField(default=0)),
                ('basic_attack', models.CharField(max_length=3)),
                ('user', models.OneToOneField(related_name=b'monster', null=True, blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='character',
            name='user',
            field=models.OneToOneField(related_name=b'character', null=True, blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
