# Generated by Django 4.2.2 on 2023-07-24 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0003_alter_propietario_apellido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edificio',
            name='tipo',
            field=models.CharField(choices=[('residencial', 'Residencial'), ('comercial', 'Comercial'), ('negocio', 'Negocio')], max_length=30),
        ),
    ]
