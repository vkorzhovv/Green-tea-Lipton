# Generated by Django 4.1.7 on 2023-02-18 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_city_profile_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='manager',
            field=models.BooleanField(default=False, verbose_name='Является руководством?'),
        ),
    ]