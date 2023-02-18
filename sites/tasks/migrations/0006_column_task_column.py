# Generated by Django 4.1.7 on 2023-02-18 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_alter_comment_options_alter_task_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('order', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='column',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.column'),
        ),
    ]
