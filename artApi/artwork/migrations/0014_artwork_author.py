# Generated by Django 4.1.7 on 2023-02-24 23:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artwork', '0013_alter_artist_birth_data_alter_artist_portrait'),
    ]

    operations = [
        migrations.AddField(
            model_name='artwork',
            name='author',
            field=models.ForeignKey(default='test', on_delete=django.db.models.deletion.CASCADE, to='artwork.artist'),
            preserve_default=False,
        ),
    ]
