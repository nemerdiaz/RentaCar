# Generated by Django 2.2.7 on 2019-11-17 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('renta', '0002_auto_20191117_0407'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persona',
            name='comentarios',
        ),
        migrations.AlterField(
            model_name='persona',
            name='run',
            field=models.IntegerField(max_length=9, unique=True),
        ),
    ]
