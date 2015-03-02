# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20150301_0331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='content',
            field=models.TextField(validators=[django.core.validators.MinLengthValidator(5)]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='journal',
            name='title',
            field=models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(2)]),
            preserve_default=True,
        ),
    ]
