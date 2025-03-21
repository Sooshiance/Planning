# Generated by Django 5.1.7 on 2025-03-18 21:00

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pid',
            field=models.CharField(default=uuid.UUID('b43d50c9-a7ba-436b-a67f-806942b08b65'), max_length=25, unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
