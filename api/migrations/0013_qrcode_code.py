# Generated by Django 2.2.5 on 2019-10-10 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20191010_2128'),
    ]

    operations = [
        migrations.AddField(
            model_name='qrcode',
            name='code',
            field=models.ImageField(blank=True, null=True, upload_to='qr'),
        ),
    ]
