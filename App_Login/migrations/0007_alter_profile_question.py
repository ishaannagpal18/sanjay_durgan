# Generated by Django 3.2.7 on 2022-02-11 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Login', '0006_remove_profile_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='question',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
