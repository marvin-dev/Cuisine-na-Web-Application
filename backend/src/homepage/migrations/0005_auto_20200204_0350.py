# Generated by Django 2.2.8 on 2020-02-04 03:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_remove_account_age'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ratingandreview',
            old_name='account',
            new_name='commentor',
        ),
    ]
