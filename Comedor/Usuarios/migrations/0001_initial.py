# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('Nombre', models.CharField(max_length=60)),
                ('Apellido', models.CharField(max_length=60)),
                ('Dni', models.IntegerField()),
                ('User_id', models.AutoField(serialize=False, primary_key=True)),
                ('Telefono', models.IntegerField()),
                ('Nacimiento', models.DateField()),
                ('Condicion', models.CharField(default=b'ES', max_length=20, choices=[(b'ES', b'Estudiante'), (b'BE', b'Becado'), (b'DO', b'Docente')])),
                ('Saldo', models.IntegerField(default=0)),
            ],
        ),
    ]
