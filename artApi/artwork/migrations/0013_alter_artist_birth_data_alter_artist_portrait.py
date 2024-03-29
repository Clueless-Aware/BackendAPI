# Generated by Django 4.1.7 on 2023-02-24 23:49

import artwork.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artwork', '0012_remove_artwork_artist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='birth_data',
            field=models.CharField(db_column='birth data', max_length=128),
        ),
        migrations.AlterField(
            model_name='artist',
            name='portrait',
            field=models.ImageField(max_length=64, upload_to=artwork.models.upload_to),
        ),
    ]
