# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Comidas', '0002_auto_20150905_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='comida',
            name='C_Guarnicion',
            field=models.ForeignKey(default=2, to='Comidas.Guarnicion'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comida',
            name='C_Postre',
            field=models.ForeignKey(default=2, to='Comidas.Postre'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comida',
            name='C_Ppal',
            field=models.ForeignKey(default=1, to='Comidas.PlatoPrincipal'),
            preserve_default=False,
        ),
    ]
