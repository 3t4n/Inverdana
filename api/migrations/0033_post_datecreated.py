# Generated by Django 2.2.5 on 2019-11-26 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0032_auto_20191125_1756'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='dateCreated',
            field=models.DateField(auto_now_add=True, default='2015-06-22'),
            preserve_default=False,
        ),
    ]
