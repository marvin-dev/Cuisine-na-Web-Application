# Generated by Django 2.2.8 on 2020-01-30 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_auto_20200129_0211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='age',
        ),
    ]