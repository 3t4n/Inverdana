# Generated by Django 2.2.5 on 2019-11-27 11:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20191127_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clans', to=settings.AUTH_USER_MODEL, verbose_name='Personas'),
        ),
    ]