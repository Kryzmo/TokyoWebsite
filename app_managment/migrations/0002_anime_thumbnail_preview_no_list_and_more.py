# Generated by Django 4.0.4 on 2023-05-23 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_managment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='thumbnail_preview_no_list',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='episode',
            name='thumbnail_preview_no_list',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
