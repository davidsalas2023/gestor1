# Generated by Django 5.0 on 2023-12-15 02:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estacionamiento',
            fields=[
                ('patente', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('modelo_auto', models.CharField(max_length=50)),
                ('tipo_usuario', models.CharField(choices=[('Visita', 'Visita'), ('Residente', 'Residente'), ('Externo', 'Externo')], max_length=20)),
                ('contacto', models.CharField(max_length=20)),
                ('nombre_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Usuarios.usuario')),
            ],
        ),
    ]