# Generated by Django 2.2.5 on 2019-11-23 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_auto_20191122_1113'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suggestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=300)),
            ],
            options={
                'verbose_name': 'Sugerencia',
                'verbose_name_plural': 'Sugerencias',
            },
        ),
        migrations.AlterModelOptions(
            name='treestate',
            options={'verbose_name': 'estado', 'verbose_name_plural': 'Estados catálogo'},
        ),
        migrations.AlterField(
            model_name='tree',
            name='age',
            field=models.IntegerField(default=0, verbose_name='Edad'),
        ),
        migrations.AlterField(
            model_name='tree',
            name='specie_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.TreeSpecie', verbose_name='Especie'),
        ),
    ]