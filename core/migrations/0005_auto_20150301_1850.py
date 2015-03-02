# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20150301_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='content',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='journal',
            name='title',
            field=models.CharField(max_length=255),
            preserve_default=True,
        ),
    ]
