# Generated by Django 2.2.5 on 2019-12-08 19:29

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Clan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('info', models.TextField(max_length=300)),
                ('photo', models.ImageField(null=True, upload_to='clans')),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Clan',
                'verbose_name_plural': 'Clans',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('info', models.TextField(max_length=900, verbose_name='Descripción')),
                ('size', models.IntegerField(default=0, verbose_name='Cantidad de Asistentes')),
                ('initial_date', models.DateTimeField(verbose_name='Fecha Inicial')),
                ('final_date', models.DateTimeField(verbose_name='Fecha Final')),
                ('place', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('photo', models.ImageField(upload_to='events')),
            ],
            options={
                'verbose_name': 'Evento',
                'verbose_name_plural': 'Eventos',
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre Organización')),
                ('info', models.TextField(max_length=900, verbose_name='Descripción')),
                ('legalrep', models.CharField(max_length=100, verbose_name='Representante')),
                ('number', models.CharField(max_length=100, verbose_name='Número de teléfono')),
            ],
            options={
                'verbose_name': 'Organización',
                'verbose_name_plural': 'Organizaciones',
            },
        ),
        migrations.CreateModel(
            name='Suggestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=300)),
                ('seen', models.BooleanField(default=False)),
                ('dateCreated', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Sugerencia',
                'verbose_name_plural': 'Sugerencias',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.TextField(max_length=300)),
                ('photo', models.ImageField(null=True, upload_to='posts')),
                ('dateCreated', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
        migrations.CreateModel(
            name='MemberShip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateField(auto_now_add=True)),
                ('invite_reason', models.CharField(max_length=64)),
                ('clan_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Clan', verbose_name='Clan')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clans', to=settings.AUTH_USER_MODEL, verbose_name='Personas')),
            ],
            options={
                'verbose_name': 'Membresía',
                'verbose_name_plural': 'Membresías',
            },
        ),
    ]
