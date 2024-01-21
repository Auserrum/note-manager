# Generated by Django 5.0 on 2024-01-12 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_task_completed_task_deleted'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.RemoveField(
            model_name='task',
            name='completed',
        ),
        migrations.RemoveField(
            model_name='task',
            name='deleted',
        ),
        migrations.RemoveField(
            model_name='task',
            name='is_delete',
        ),
        migrations.RemoveField(
            model_name='task',
            name='is_gone',
        ),
        migrations.AddField(
            model_name='task',
            name='content',
            field=models.TextField(default='', verbose_name='Текст'),
        ),
    ]