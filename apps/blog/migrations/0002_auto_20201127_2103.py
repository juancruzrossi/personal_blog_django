# Generated by Django 3.1.3 on 2020-11-28 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='apellidos',
            field=models.CharField(max_length=255, verbose_name='Apellido de Autor'),
        ),
        migrations.AlterField(
            model_name='autor',
            name='nombres',
            field=models.CharField(max_length=255, verbose_name='Nombre de Autor'),
        ),
    ]
