# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=120)),
                ('xp', models.IntegerField(default=0)),
                ('level', models.IntegerField(default=1)),
                ('gp', models.IntegerField(default=0)),
                ('str', models.IntegerField(default=0)),
                ('int', models.IntegerField(default=0)),
                ('agl', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('str', models.IntegerField(default=0)),
                ('str_multiplier', models.FloatField(default=0)),
                ('int', models.IntegerField(default=0)),
                ('int_multiplier', models.FloatField(default=0)),
                ('agl', models.IntegerField(default=0)),
                ('agl_multiplier', models.IntegerField(default=0)),
                ('basic_attack', models.CharField(max_length=3)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Mob',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=120)),
                ('str', models.IntegerField(default=0)),
                ('int', models.IntegerField(default=0)),
                ('agl', models.IntegerField(default=0)),
                ('basic_attack', models.CharField(max_length=3)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=120)),
                ('level', models.IntegerField(default=0)),
                ('description', models.TextField()),
                ('kind', models.CharField(max_length=3)),
                ('multiplier', models.FloatField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=120)),
                ('level', models.IntegerField(default=1)),
                ('xp_drop', models.IntegerField(default=0)),
                ('gp_drop', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='mob',
            name='zone',
            field=models.ForeignKey(related_name=b'mobs', to='college_life.Zone'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='major',
            name='skills',
            field=models.ForeignKey(related_name=b'class', to='college_life.Skill'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='character',
            name='major',
            field=models.ForeignKey(related_name=b'characters', to='college_life.Major'),
            preserve_default=True,
        ),
    ]
