# Generated by Django 4.0.4 on 2022-05-29 12:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VicHubApp', '0004_alter_user_date_of_birth_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2022, 5, 29, 14, 42, 45, 460553)),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_of_promotion',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 29, 14, 42, 45, 460552)),
        ),
    ]