# Generated by Django 4.1.1 on 2023-12-18 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0006_solicitud'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='tipo',
            field=models.CharField(choices=[('estacionamiento', 'estacionamiento'), ('administracion', 'administracion'), ('administrador', 'administrador')], max_length=20),
        ),
    ]