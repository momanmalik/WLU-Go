# Generated by Django 3.2.6 on 2021-08-13 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wlugoapp', '0006_auto_20210812_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='mean_user_score',
            field=models.IntegerField(),
        ),
    ]
