from django.core.files import File
from urllib.request import urlopen
from tempfile import NamedTemporaryFile
from django.contrib import admin
from .forms import *
from .models import *
import requests
# Register your models here.


def get_content_type(url):
    return requests.head(url).headers['Content-Type']

class AnimeAdmin(admin.ModelAdmin):
    form = AnimeForms
    fields = ['mal', 'alternative_name', 'tags', 'studio','slug', 'name', 'shinden', 'description', 'type', 'episodes', 'status', 'aired', 'source', 'image', 'thumbnail_anime_preview']
    readonly_fields = ['slug', 'name', 'alternative_name', 'shinden','description', 'type', 'episodes', 'status', 'aired', 'source', 'tag_str', 'studio_str', 'thumbnail_anime_preview']
    filter_horizontal = ['tags', 'studio']

    def save_related(self, request, form: AnimeForms, formsets, change):
        self_pub_id = request.resolver_match.args
        super(AnimeAdmin, self).save_related(request, form, formsets, change)
        form.instance.tags.add(*list(form.instance.tag_str))
        form.instance.studio.add(*list(form.instance.studio_str))
        img_temp = NamedTemporaryFile(delete=True)
        img_temp.write(urlopen(form.instance.image_url).read())
        img_temp.flush()
        form.instance.image.save(f"image_{form.instance.name}.webp", File(img_temp))
        form.instance.image.close

class TagAdmin(admin.ModelAdmin):
    readonly_fields = ['slug']

class StudiosAdmin(admin.ModelAdmin):
    readonly_fields = ['slug']

class EpisodeAnime(admin.ModelAdmin):
    form = EpisodeForms
    fields = ['anime', 'title', 'translator', 'proofreader', 'typesetting', 'description',  'japanese_language', 'episode_number', 'image_url', 'image', 'thumbnail_episode_preview']
    filter_horizontal = ['translator', 'proofreader', 'typesetting']
    readonly_fields = ['slug', 'aired', 'title', 'player', 'thumbnail_episode_preview']

    def save_related(self, request, form: EpisodeForms, formsets, change):
        self_pub_id = request.resolver_match.args
        super(EpisodeAnime, self).save_related(request, form, formsets, change)
        if not form.instance.image:
            img_temp = NamedTemporaryFile(delete=True)
            extension = "gif" if "gif" in get_content_type(form.instance.image_url) else "webp"
            img_temp.write(urlopen(form.instance.image_url).read())
            img_temp.flush()
            form.instance.image.save(f"image_{form.instance.title}.{extension}", File(img_temp))
            form.instance.image.close

admin.site.register(Anime, AnimeAdmin)
admin.site.register(Episode, EpisodeAnime)
admin.site.register(Tag, TagAdmin)
admin.site.register(Studios, StudiosAdmin)
admin.site.register(Crew)