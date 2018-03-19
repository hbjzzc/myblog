# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20180318_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='user',
            field=models.ForeignKey(verbose_name='文章作者', to='myapp.User'),
        ),
    ]
