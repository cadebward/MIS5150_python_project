# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150301_0330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='last_edited',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='journal',
            name='publish_date',
            field=models.DateTimeField(null=True, verbose_name=b'date published', blank=True),
            preserve_default=True,
        ),
    ]
