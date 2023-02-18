# Generated by Django 4.1.7 on 2023-02-18 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notificationuser',
            name='create',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='notificationuser',
            name='send_datetime',
            field=models.DateTimeField(verbose_name='Дата отправки'),
        ),
        migrations.AlterField(
            model_name='notificationuser',
            name='send_status',
            field=models.BooleanField(default=True, verbose_name='Статус отправки'),
        ),
    ]