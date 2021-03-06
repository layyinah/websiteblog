# Generated by Django 2.2 on 2021-08-04 14:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('desc', models.TextField()),
                ('img', models.ImageField(upload_to='blog')),
                ('auth', models.CharField(max_length=255)),
                ('date', models.DateField(default=datetime.date.today)),
            ],
            options={
                'verbose_name': 'blog',
                'verbose_name_plural': 'blogs',
                'ordering': ('name',),
            },
        ),
    ]
