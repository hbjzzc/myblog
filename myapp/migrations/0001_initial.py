# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('headline', models.CharField(verbose_name='标题', max_length=20)),
                ('author', models.CharField(verbose_name='作者', max_length=20)),
                ('contents', models.CharField(verbose_name='内容', max_length=10000)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
            ],
            options={
                'db_table': 'titles',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='姓名', max_length=20)),
                ('desc', models.CharField(verbose_name='个人简历', max_length=100)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
