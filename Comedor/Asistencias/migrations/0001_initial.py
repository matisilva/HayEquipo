# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '__first__'),
        ('Comidas', '0003_auto_20150905_1632'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('A_fecha', models.DateTimeField(auto_now_add=True)),
                ('A_id', models.ForeignKey(to='Usuarios.Usuario')),
                ('A_menu', models.ForeignKey(to='Comidas.Comida')),
            ],
        ),
    ]
