# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('djangui', '0002_remove_scriptparameter_output_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='script',
            name='slug',
            field=autoslug.fields.AutoSlugField(populate_from=b'script_name', unique=True, editable=False),
        ),
        migrations.AlterField(
            model_name='scriptgroup',
            name='slug',
            field=autoslug.fields.AutoSlugField(populate_from=b'group_name', unique=True, editable=False),
        ),
        migrations.AlterField(
            model_name='scriptparameter',
            name='slug',
            field=autoslug.fields.AutoSlugField(populate_from=b'script_param', unique=True, editable=False),
        ),
    ]
