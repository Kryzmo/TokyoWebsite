# Generated by Django 4.0.4 on 2023-05-23 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_managment', '0002_anime_thumbnail_preview_no_list_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crew',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, null=True)),
                ('description', models.TextField(max_length=2000, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='crew_avatars/')),
                ('slug', models.SlugField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'verbose_name': 'Anime group',
                'verbose_name_plural': 'Anime groups',
            },
        ),
        migrations.RemoveField(
            model_name='episode',
            name='groups',
        ),
        migrations.DeleteModel(
            name='AnimeGroups',
        ),
        migrations.AddField(
            model_name='episode',
            name='proofreader',
            field=models.ManyToManyField(related_name='crew_proofreader', to='app_managment.crew'),
        ),
        migrations.AddField(
            model_name='episode',
            name='translator',
            field=models.ManyToManyField(related_name='crew_translator', to='app_managment.crew'),
        ),
        migrations.AddField(
            model_name='episode',
            name='typesetting',
            field=models.ManyToManyField(blank=True, related_name='crew_typesetting', to='app_managment.crew'),
        ),
    ]
