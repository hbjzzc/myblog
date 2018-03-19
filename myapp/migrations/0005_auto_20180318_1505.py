# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20180317_0011'),
    ]

    operations = [
        migrations.RenameField(
            model_name='title',
            old_name='user',
            new_name='user_id',
        ),
    ]
