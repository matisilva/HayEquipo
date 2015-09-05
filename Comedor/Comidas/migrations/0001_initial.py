# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comida',
            fields=[
                ('C_id', models.AutoField(serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Guarnicion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Descripcion', models.CharField(max_length=30)),
                ('Ingredientes', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PlatoPrincipal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Descripcion', models.CharField(max_length=30)),
                ('Ingredientes', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Postre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Descripcion', models.CharField(max_length=30)),
            ],
        ),
    ]
