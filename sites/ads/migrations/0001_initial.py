# Generated by Django 4.1.7 on 2023-02-18 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('importance', models.IntegerField(choices=[(1, 'Low'), (2, 'Medium'), (3, 'High')], default=1)),
                ('is_published', models.BooleanField(default=False)),
                ('publication_date', models.DateField(blank=True, null=True)),
                ('send_email_notification', models.BooleanField(default=False)),
                ('send_telegram_notification', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
