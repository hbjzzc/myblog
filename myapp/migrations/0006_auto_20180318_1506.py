# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20180318_1505'),
    ]

    operations = [
        migrations.RenameField(
            model_name='title',
            old_name='user_id',
            new_name='user',
        ),
    ]
