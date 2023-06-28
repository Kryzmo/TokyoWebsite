from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils.safestring import mark_safe


# Create your models here.

class Crew(models.Model):
    def __str__(self):
        return f"{self.name}"

    name = models.CharField(max_length=70, null=True)
    description = models.TextField(max_length=2000, null=True)
    image = models.ImageField(upload_to='crew_avatars/', null=True, blank=True)
    slug = models.SlugField(max_length=1000, null=True, blank=True)


    class Meta():
        verbose_name = "Anime group"
        verbose_name_plural = "Anime groups"

    
class Tag(models.Model):
    def __str__(self):
        return self.tag_name
        
    tag_name = models.CharField(max_length=70, null=True)
    description = models.TextField(max_length=2000, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    slug = models.SlugField(max_length=1000, null=True)

    class Meta():
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

class Studios(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=300, null=True)
    description = models.TextField(max_length=2000, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    slug = models.SlugField(max_length=1000, null=True)

    class Meta():
        verbose_name = "Studio"
        verbose_name_plural = "Studios"

class Anime(models.Model):
    def __str__(self):
        if self.name==None:
            return "ERROR-ANIME NAME IS NULL"
        return self.name

    mal = models.CharField(max_length=300, null=True, blank=True)
    shinden = models.CharField(max_length=300, null=True, blank=True)
    name = models.CharField(max_length=300, null=True, blank=True)
    alternative_name = ArrayField(models.CharField(max_length=300, default=None), size=20, null=True, blank=True)
    tags = models.ManyToManyField(Tag, related_name='tagging', blank=True, unique=False)
    description = models.TextField(max_length=2000, null=True, blank=True)
    type = models.CharField(max_length=30, null=True, blank=True)
    episodes = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True)
    aired = models.DateField(null=True, blank=True)
    studio = models.ManyToManyField(Studios, related_name='studioos', blank=True, unique=False)
    source = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(upload_to='image/', null=True, blank=True)
    image_url = models.URLField(blank=True, max_length=600)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    slug = models.SlugField(max_length=1000, null=True, blank=True)
    tag_str = models.CharField(max_length=300, null=True, blank=True)
    studio_str = models.CharField(max_length=300, null=True, blank=True)
    thumbnail_preview_no_list = models.CharField(blank=True, max_length=1000)



    class Meta():
        verbose_name = "Anime"
        verbose_name_plural = "Animes"
    
    def thumbnail_anime_preview(self):
        if self.image:
            return mark_safe('<img id="imgsrc" src="%s" style="max-width: 400px; max-height: 300px;"/><script>function changeValue(){document.getElementById("imgsrc").src = document.getElementById("liveimg").value;}</script>' % (f"/media/{self.image}"))
        return mark_safe('<img id="imgsrc" src="" style="max-width: 400px; max-height: 300px;"/><script>function changeValue(){document.getElementById("imgsrc").src = document.getElementById("liveimg").value;}</script>')
    thumbnail_anime_preview.help_text = 'baka'
    thumbnail_anime_preview.short_description = 'Podglad Obrazka'
    thumbnail_anime_preview.allow_tags = True

class Episode(models.Model):
    def __str__(self):
        if self.anime==None:
            return "ERROR-EPISODE NAME IS NULL"
        return f"{self.anime.name} Odcinek {self.correct_number}" 

    anime = models.ForeignKey(Anime, related_name='Animes', on_delete=models.CASCADE)
    title = models.CharField(max_length=300, blank=True)
    translator = models.ManyToManyField(Crew, related_name='crew_translator', unique=False)
    proofreader = models.ManyToManyField(Crew, related_name='crew_proofreader', unique=False)
    typesetting = models.ManyToManyField(Crew, related_name='crew_typesetting', blank=True, unique=False)
    description = models.TextField(max_length=506, help_text="Maksymalna dlugosc opisu wynosi 506 znakow")
    aired = models.DateField(null=True, blank=True)
    japanese_language = models.BooleanField(default=True)
    episode_number = models.DecimalField(default=1, max_digits=5, decimal_places=1)
    image = models.ImageField(upload_to='episode_thumbnail/', null=True, blank=True)
    image_url = models.URLField(blank=True, max_length=600)
    player = models.CharField(max_length=2500, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    slug = models.SlugField(max_length=1000, null=True, blank=True)
    thumbnail_preview_no_list = models.CharField(blank=True, max_length=1000)

    class Meta():
        verbose_name = "Episode"
        verbose_name_plural = "Episodes"

    @property
    def correct_number(self):
        if "0.5" not in f"{self.episode_number}":
            return int(self.episode_number)
        else:
            return self.episode_number
        
    def thumbnail_episode_preview(self):
        if self.image:
            return mark_safe('<img id="imgsrc" src="%s" style="max-width: 400px; max-height: 300px;"/><script>function changeValue(){document.getElementById("imgsrc").src = document.getElementById("liveimg").value;}</script>' % (f"/media/{self.image}"))
        return mark_safe('<img id="imgsrc" src="" style="max-width: 400px; max-height: 300px;"/><script>function changeValue(){document.getElementById("imgsrc").src = document.getElementById("liveimg").value;}</script>')
    thumbnail_episode_preview.help_text = 'baka'
    thumbnail_episode_preview.short_description = 'Podglad Obrazka'
    thumbnail_episode_preview.allow_tags = True