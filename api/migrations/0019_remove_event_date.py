# Generated by Django 2.2.5 on 2019-11-21 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_event_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='date',
        ),
    ]
