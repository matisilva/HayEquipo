# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='Condicion',
            field=models.CharField(default=b'ES', max_length=1, choices=[(b'ES', b'Estudiante'), (b'BE', b'Becado'), (b'DO', b'Docente')]),
        ),
    ]
