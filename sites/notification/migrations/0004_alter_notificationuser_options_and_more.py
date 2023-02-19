# Generated by Django 4.1.7 on 2023-02-19 00:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_profile_phone_alter_profile_photo_and_more'),
        ('notification', '0003_alter_notification_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notificationuser',
            options={'ordering': ['send_datetime']},
        ),
        migrations.AlterField(
            model_name='notificationuser',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notification', to='users.profile', verbose_name=''),
        ),
    ]