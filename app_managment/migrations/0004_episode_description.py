# Generated by Django 4.0.4 on 2023-05-23 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_managment', '0003_crew_remove_episode_groups_delete_animegroups_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='description',
            field=models.TextField(null=True, help_text='Maksymalna dlugosc opisu wynosi 506 znakow', max_length=506),
            preserve_default=False,
        ),
    ]
