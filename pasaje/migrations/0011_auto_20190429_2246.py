# Generated by Django 2.2 on 2019-04-30 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pasaje', '0010_trayecto_horario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viaje',
            name='fecha',
            field=models.DateField(),
        ),
    ]
