# Generated by Django 5.0 on 2023-12-18 19:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('culinarists', '0002_experience'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='experience',
            options={'verbose_name_plural': 'experiences'},
        ),
        migrations.AddField(
            model_name='experience',
            name='rating',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
