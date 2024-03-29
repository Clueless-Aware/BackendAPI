# Generated by Django 4.1.7 on 2023-02-26 19:54

import artwork.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artwork', '0014_artwork_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artwork',
            name='color',
        ),
        migrations.RemoveField(
            model_name='artwork',
            name='file_dimension',
        ),
        migrations.RemoveField(
            model_name='artwork',
            name='museum',
        ),
        migrations.RemoveField(
            model_name='artwork',
            name='resolution',
        ),
        migrations.RemoveField(
            model_name='artwork',
            name='size',
        ),
        migrations.AddField(
            model_name='artwork',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='artwork',
            name='form',
            field=models.CharField(default='test', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='artwork',
            name='location',
            field=models.CharField(default='test', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='artwork',
            name='technique',
            field=models.CharField(default='test', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='artwork',
            name='timeframe',
            field=models.CharField(default='test', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='artwork',
            name='date',
            field=models.CharField(default='test', max_length=128),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='artwork',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='artwork',
            name='image_url',
            field=models.ImageField(db_column='jpg url', max_length=254, upload_to=artwork.models.upload_to),
        ),
    ]
