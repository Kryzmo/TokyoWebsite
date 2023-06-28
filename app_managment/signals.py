from django.utils.text import slugify
from django.db.models.signals import pre_save, post_delete, post_save, m2m_changed
from django.http import HttpResponseRedirect
from django.dispatch import receiver
from .models import *
from pathlib import Path
import os
import requests
import json
import re
import datetime
from app_managment.error_handler import Error

@receiver(pre_save, sender=Anime)
def anime_pre_save(sender, instance: Anime, *args, **kwargs):
    while True:
        for r in range(1):
            try:
                get_id = re.findall('\d+', instance.mal)
                anime_id = get_id[0]
                api_url = 'https://api.jikan.moe/v4/anime/{}'.format(anime_id)
                headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.117',
                'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language' : 'en-US,en;q=0.5',
                'Accept-Encoding' : 'gzip',
                'DNT' : '1', # Do Not Track Request Header
                'Connection' : 'close' }
                r = requests.get(api_url, headers=headers)
                r_json = r.json()
                #Json extract
                alt_name = []
                r_json = r_json['data']
                anime_title = r_json['title']
                anime_source = r_json['source']
                anime_eng_title = r_json['title_english']
                anime_japanese_title = r_json['title_japanese']
                anime_synonyms_title_list = r_json['title_synonyms']
                anime_synonyms_title = ''.join(anime_synonyms_title_list)
                anime_episodes = r_json['episodes']
                anime_type = r_json['type']
                anime_tags_all = [genres["name"] for genres in r_json["genres"]]
                anime_tags = ', '.join(anime_tags_all)
                anime_status = r_json['status']
                anime_airing = r_json['airing']
                anime_aired_from = r_json['aired']['from']
                print('\nTitle: ' + str(anime_title) + '\n' + 'English Title: ' + str(anime_eng_title) + '\n' + 'Japanese Title: ' + str(anime_japanese_title) + '\n' + 'Synonyms Title: ' + str(anime_synonyms_title) + '\n' + 'Episodes: ' + str(anime_episodes) + '\n' + 'Type: ' + str(anime_type) + '\n' + 'Tags: ' + str(anime_tags) + '\n' + 'Status: ' + str(anime_status) + '\n')
                try:
                    anime_img = r_json['images']['jpg']['large_image_url']
                except:
                    anime_img = r_json['images']['jpg']['image_url']
                anime_popularity = r_json['popularity']
            
            
                for alt_titles in r_json["titles"]:
                    if alt_titles['type'] == "Synonym" or alt_titles == "English":
                        alt_name.append(alt_titles['title'])
                alt_name.append(anime_japanese_title)
                tagg = []
                studioo = []
            
                tags = [genres["name"] for genres in r_json["genres"]]
                studios = [studio["name"] for studio in r_json["studios"]]
                for _tags in tags:
                    check_tags = Tag.objects.filter(tag_name=_tags)
                    if check_tags.exists():
                        for i in check_tags:
                            tagg.append(i.id)
                    else:
                        n = Tag.objects.create(tag_name=_tags)
                        tagg.append(n.id)
                for _studios in studios:
                    check_studios = Studios.objects.filter(name=_studios)
                    # print(check_studios)
                    # print(_studios)
                    if check_studios.exists():
                        for i in check_studios:
                            studioo.append(i.id)
                    else:
                        n = Studios.objects.create(name=_studios)
                        studioo.append(n.id)
                #instance func

                instance.name = anime_title
                instance.alternative_name = alt_name
                instance.type = anime_type
                instance.episodes = anime_episodes
                instance.status = anime_status
                instance.image_url = r_json['images']['webp']['large_image_url']
                # print(r_json['images']['webp']['large_image_url'])
                instance.aired = datetime.datetime.strptime(f"{anime_aired_from[:-15]}", '%Y-%m-%d')
                instance.source = anime_source
                instance.tag_str = tagg
                instance.studio_str = studioo
                if not instance.slug:
                    instance.slug = slugify(instance.name)
                return
            except Exception as e:
                Error(e)
                continue
        else:
            print('\nMy Anime List Error\n\n')
            break

@receiver(pre_save, sender=Tag)
def tags_pre_save(sender, instance: Tag, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.tag_name)

@receiver(pre_save, sender=Studios)
def studios_pre_save(sender, instance: Studios, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)

@receiver(pre_save, sender=Episode)
def episode_pre_save(sender, instance: Episode, *args, **kwargs):
    if instance.anime.type != "Movie":
        get_id = re.findall('\d+', instance.anime.mal)
        anime_id = get_id[0]
        print(instance.correct_number)
        print(type(instance.correct_number))
        api_url = 'https://api.jikan.moe/v4/anime/{}/episodes/{}'.format(anime_id, instance.correct_number)
        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.117',
        'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language' : 'en-US,en;q=0.5',
        'Accept-Encoding' : 'gzip',
        'DNT' : '1', # Do Not Track Request Header
        'Connection' : 'close' }
        try:
            r = requests.get(api_url, headers=headers)
            r_json = r.json()
            instance.title = r_json['data']['title']
            instance.aired = datetime.datetime.strptime(f"{r_json['data']['aired'][:-15]}", '%Y-%m-%d')
        except:
            instance.title = "None"
            instance.aired = "9999-12-31"
    if instance.anime.type == "Movie":
        instance.title = instance.anime.name

    if not instance.slug:
        szlugi = '{}'.format(instance.anime.name)
        test = slugify(szlugi)
        instance.slug = test
    # print(test)

@receiver(pre_save, sender=Crew)
def crew_pre_save(sender, instance: Crew, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)