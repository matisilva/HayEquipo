# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Comidas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comida',
            old_name='C_id',
            new_name='Comida_id',
        ),
    ]
