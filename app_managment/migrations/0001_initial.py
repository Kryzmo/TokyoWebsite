# Generated by Django 4.0.4 on 2023-05-23 21:48

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mal', models.CharField(blank=True, max_length=300, null=True)),
                ('shinden', models.CharField(blank=True, max_length=300, null=True)),
                ('name', models.CharField(blank=True, max_length=300, null=True)),
                ('alternative_name', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(default=None, max_length=300), blank=True, null=True, size=20)),
                ('description', models.TextField(blank=True, max_length=2000, null=True)),
                ('type', models.CharField(blank=True, max_length=30, null=True)),
                ('episodes', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=50, null=True)),
                ('aired', models.DateField(blank=True, null=True)),
                ('source', models.CharField(blank=True, max_length=50, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('image_url', models.URLField(blank=True, max_length=600)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('slug', models.SlugField(blank=True, max_length=1000, null=True)),
                ('tag_str', models.CharField(blank=True, max_length=300, null=True)),
                ('studio_str', models.CharField(blank=True, max_length=300, null=True)),
            ],
            options={
                'verbose_name': 'Anime',
                'verbose_name_plural': 'Animes',
            },
        ),
        migrations.CreateModel(
            name='AnimeGroups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, null=True)),
                ('description', models.TextField(max_length=2000, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='group_logos/')),
                ('slug', models.SlugField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'verbose_name': 'Anime group',
                'verbose_name_plural': 'Anime groups',
            },
        ),
        migrations.CreateModel(
            name='Studios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, null=True)),
                ('description', models.TextField(max_length=2000, null=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('slug', models.SlugField(max_length=1000, null=True)),
            ],
            options={
                'verbose_name': 'Studio',
                'verbose_name_plural': 'Studios',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=70, null=True)),
                ('description', models.TextField(max_length=2000, null=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('slug', models.SlugField(max_length=1000, null=True)),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=300)),
                ('aired', models.DateField(blank=True, null=True)),
                ('japanese_language', models.BooleanField(default=True)),
                ('episode_number', models.DecimalField(decimal_places=1, default=1, max_digits=5)),
                ('image', models.ImageField(blank=True, null=True, upload_to='episode_thumbnail/')),
                ('image_url', models.URLField(blank=True, max_length=600)),
                ('player', models.CharField(blank=True, max_length=2500)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('slug', models.SlugField(blank=True, max_length=1000, null=True)),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Animes', to='app_managment.anime')),
                ('groups', models.ManyToManyField(blank=True, to='app_managment.animegroups')),
            ],
            options={
                'verbose_name': 'Episode',
                'verbose_name_plural': 'Episodes',
            },
        ),
        migrations.AddField(
            model_name='anime',
            name='studio',
            field=models.ManyToManyField(blank=True, related_name='studioos', to='app_managment.studios'),
        ),
        migrations.AddField(
            model_name='anime',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tagging', to='app_managment.tag'),
        ),
    ]
