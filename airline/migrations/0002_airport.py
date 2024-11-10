# Generated by Django 4.2.5 on 2024-11-10 11:13

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('airline', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=150, unique=True)),
                ('city_name', models.CharField(max_length=150)),
                ('code', models.CharField(max_length=3, unique=True, validators=[django.core.validators.RegexValidator(message='Airline code must be exactly three uppercase letters (IATA standard)', regex='^[A-Z]{3}$')])),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
