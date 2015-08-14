# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0002_auto_20150813_1117'),
    ]

    operations = [
        migrations.AddField(
            model_name='sphere',
            name='discription',
            field=models.TextField(blank=True),
        ),
    ]
