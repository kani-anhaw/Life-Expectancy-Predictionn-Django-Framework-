# Generated by Django 4.1.5 on 2023-01-26 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predresult',
            name='b',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='predresult',
            name='u',
            field=models.FloatField(),
        ),
    ]