# Generated by Django 3.2.6 on 2021-08-12 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wlugoapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='course_id',
            field=models.UUIDField(),
        ),
        migrations.AlterField(
            model_name='rating',
            name='user_id',
            field=models.UUIDField(),
        ),
    ]
