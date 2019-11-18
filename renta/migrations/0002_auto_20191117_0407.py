# Generated by Django 2.2.7 on 2019-11-17 07:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('renta', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='direccion',
            name='comunaOrigen',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='persona',
            name='run',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='renta.Direccion', unique=True),
        ),
    ]