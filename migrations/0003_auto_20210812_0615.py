# Generated by Django 3.2.6 on 2021-08-12 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wlugoapp', '0002_auto_20210812_0022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor_course',
            name='course_id',
            field=models.UUIDField(),
        ),
        migrations.AlterField(
            model_name='professor_course',
            name='professor_id',
            field=models.UUIDField(),
        ),
    ]
