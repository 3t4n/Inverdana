# Generated by Django 2.2.5 on 2019-10-20 20:14

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_auto_20191020_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worldborder',
            name='mpoly',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(null=True, srid=4326),
        ),
    ]