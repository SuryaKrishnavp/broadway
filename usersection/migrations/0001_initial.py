# Generated by Django 5.1.2 on 2024-10-14 06:59

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Userinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=50, unique=True)),
                ('Phonenumber', models.CharField(max_length=128, unique=True)),
                ('Password', models.CharField(max_length=128, validators=[django.core.validators.MinLengthValidator(8)])),
            ],
        ),
        migrations.CreateModel(
            name='Userpersonal_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Address', models.TextField(max_length=100)),
                ('Country', models.CharField(max_length=100, null=True)),
                ('District', models.CharField(max_length=100, null=True)),
                ('Place', models.CharField(max_length=100, null=True)),
                ('Id_Image', models.ImageField(null=True, upload_to='media/images')),
                ('Gender', models.CharField(max_length=20, null=True)),
                ('User_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usersection.userinfo')),
            ],
        ),
    ]
