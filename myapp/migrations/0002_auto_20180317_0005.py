# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='title',
            name='user_id',
            field=models.ForeignKey(verbose_name='文章作者', default='', to='myapp.User'),
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(verbose_name='密码', max_length=20, default=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='desc',
            field=models.CharField(verbose_name='个人简历', max_length=100, default='哈哈哈'),
        ),
    ]
