# Generated by Django 2.2.5 on 2019-10-10 21:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20191010_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qrcode',
            name='tree_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='identifier', to='api.Tree'),
        ),
    ]