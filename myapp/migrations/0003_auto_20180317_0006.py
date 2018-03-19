# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20180317_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='user_id',
            field=models.ForeignKey(verbose_name='文章作者', default=1, to='myapp.User'),
        ),
    ]
