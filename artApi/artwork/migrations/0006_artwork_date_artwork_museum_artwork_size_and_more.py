# Generated by Django 4.1.7 on 2023-02-21 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artwork', '0005_remove_artwork_author_remove_artwork_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='artwork',
            name='date',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='artwork',
            name='museum',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='artwork',
            name='size',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='artwork',
            name='type',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
