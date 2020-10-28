# Generated by Django 3.0.5 on 2020-10-28 08:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GuideData',
            fields=[
                ('guide_id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=200, unique=True)),
                ('phone_number', models.CharField(max_length=10, unique=True)),
                ('profile_pic', models.ImageField(default='no_image.png', upload_to='guide_profile_pics/')),
                ('dob', models.DateField(default=datetime.datetime.today)),
                ('address', models.TextField()),
            ],
        ),
    ]