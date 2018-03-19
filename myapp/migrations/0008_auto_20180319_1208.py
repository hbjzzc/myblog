# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20180318_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='desc',
            field=models.CharField(verbose_name='个人简历', max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(verbose_name='密码', max_length=20),
        ),
    ]
