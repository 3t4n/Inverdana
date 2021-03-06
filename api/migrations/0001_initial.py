# Generated by Django 2.2.5 on 2019-09-27 14:44

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('area', models.IntegerField(default=0)),
                ('fips', models.CharField(default='XX', max_length=2, verbose_name='FIPS Code')),
                ('iso2', models.CharField(default='XX', max_length=2, verbose_name='2 Digit ISO')),
                ('iso_3', models.CharField(default='XX', max_length=3, verbose_name='3 Digit ISO')),
                ('un', models.IntegerField(default=-1, verbose_name='United Nations Code')),
                ('region', models.IntegerField(default=-1, verbose_name='Region Code')),
                ('subregion', models.IntegerField(default=-1, verbose_name='Sub-Region Code')),
                ('location', django.contrib.gis.db.models.fields.PointField(null=True, srid=4326)),
                ('mpoly', django.contrib.gis.db.models.fields.MultiPolygonField(null=True, srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='GeoEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('geometry', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Preference',
            fields=[
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='preferences', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('push_notifications_trees', models.BooleanField(default=True)),
                ('push_notifications_events', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Share',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.BooleanField(default=True)),
                ('percentage', models.IntegerField(default=100)),
                ('dateCreated', models.DateField(auto_now_add=True)),
                ('dateModified', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TreeSpecie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commonname', models.CharField(max_length=100)),
                ('sciname', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField(default=0)),
                ('point', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('shareholders', models.ManyToManyField(related_name='shares', through='api.Share', to=settings.AUTH_USER_MODEL)),
                ('specie_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.TreeSpecie')),
            ],
        ),
        migrations.AddField(
            model_name='share',
            name='tree_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Tree'),
        ),
        migrations.AddField(
            model_name='share',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('address1', models.CharField(max_length=50)),
                ('address2', models.CharField(max_length=50)),
                ('cellphone', models.CharField(max_length=50)),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='info', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('country', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='country', to='api.Country')),
            ],
        ),
    ]
