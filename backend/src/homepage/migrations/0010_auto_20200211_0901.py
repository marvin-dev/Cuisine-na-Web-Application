# Generated by Django 2.2.8 on 2020-02-11 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0009_auto_20200207_0705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='cooking_time',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='prep_time',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='recipe_name',
            field=models.CharField(max_length=80),
        ),
    ]