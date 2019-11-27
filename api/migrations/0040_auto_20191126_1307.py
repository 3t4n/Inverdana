# Generated by Django 2.2.5 on 2019-11-26 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0039_merge_20191126_1307'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
        migrations.DeleteModel(
            name='Suggestion',
        ),
        migrations.AlterField(
            model_name='achievementcatalog',
            name='desc',
            field=models.TextField(max_length=255, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='achievementcatalog',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='achievementcatalog',
            name='photo',
            field=models.ImageField(upload_to='trees', verbose_name='Foto'),
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]