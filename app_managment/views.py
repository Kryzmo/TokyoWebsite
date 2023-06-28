from django.shortcuts import render
from app_managment.config import Config
from django.core.paginator import Paginator
from .models import *
from app_managment.error_handler import Error
from app_managment.utils import icons
# Create your views here.


def index(request):
    episodes = Episode.objects.filter().order_by('-date')
    main_new_episodes = Paginator(episodes, 4)
    qs = {
        'title': Config.website_title,
        'logo': Config.website_logo,
        'MEDIA_URL': Config.MEDIA_URL,
        'STATIC_URL': Config.STATIC_URL,
        'main_new_episodes': main_new_episodes.get_page(1),
    }
    qs.update(icons())
    return render(request, 'index.html', qs)
