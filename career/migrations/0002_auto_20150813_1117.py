# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='link',
        ),
        migrations.RemoveField(
            model_name='profession',
            name='sphere',
        ),
        migrations.AddField(
            model_name='profession',
            name='sphere',
            field=models.ManyToManyField(to='career.Sphere'),
        ),
    ]
