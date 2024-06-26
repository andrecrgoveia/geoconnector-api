# Generated by Django 4.2 on 2024-04-04 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geoconnector', '0002_pointresourcelinkstatus_points'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pointresourcelinkstatus',
            old_name='points',
            new_name='linked_points',
        ),
        migrations.RemoveField(
            model_name='pointresourcelinkstatus',
            name='resource_links',
        ),
        migrations.AddField(
            model_name='pointresourcelinkstatus',
            name='linked_resources',
            field=models.ManyToManyField(related_name='resources', to='geoconnector.resourcelink'),
        ),
    ]
