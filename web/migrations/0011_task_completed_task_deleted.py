# Generated by Django 4.2.7 on 2023-12-04 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_category_remove_task_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='completed',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='deleted',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
