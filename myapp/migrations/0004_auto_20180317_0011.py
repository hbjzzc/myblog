# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20180317_0006'),
    ]

    operations = [
        migrations.RenameField(
            model_name='title',
            old_name='user_id',
            new_name='user',
        ),
    ]
