# Generated by Django 2.1.5 on 2020-01-23 03:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('experience', models.CharField(choices=[('Beginner', 'Beginner'), ('Advanced', 'Advanced'), ('Expert', 'Expert')], default='Beginner', max_length=50)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_name', models.CharField(max_length=50)),
                ('recipe_desc', models.TextField(null=True)),
                ('recipe_img_display', models.ImageField(upload_to='')),
                ('prep_time', models.CharField(max_length=10)),
                ('cooking_time', models.CharField(max_length=10)),
                ('serving', models.IntegerField()),
                ('ingredients', models.TextField()),
                ('process', models.TextField()),
                ('pub_date', models.DateTimeField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RecipeCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_category', models.CharField(choices=[('Appetizers', 'Dish Type'), ('Snacks', 'Snacks'), ('Main Dishes', 'Main Dishes'), ('Desserts', 'Desserts'), ('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner'), ('Smoothies', 'Smoothies')], max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='recipe_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cat', to='homepage.RecipeCategory'),
        ),
    ]