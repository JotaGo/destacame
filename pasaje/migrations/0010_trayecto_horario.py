# Generated by Django 2.2 on 2019-04-29 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pasaje', '0009_remove_trayecto_horario'),
    ]

    operations = [
        migrations.AddField(
            model_name='trayecto',
            name='horario',
            field=models.TimeField(null=True),
        ),
    ]