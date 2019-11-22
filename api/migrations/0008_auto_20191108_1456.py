# Generated by Django 2.2.5 on 2019-11-08 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.DateField(default='2012-09-04'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='info',
            field=models.TextField(max_length=300),
        ),
    ]