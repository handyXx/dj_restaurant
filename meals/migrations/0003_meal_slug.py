# Generated by Django 3.2.4 on 2021-06-04 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0002_alter_meal_preperation_tim'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
