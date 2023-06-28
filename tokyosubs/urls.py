from app_managment.views import *
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    path('static/css/index.css', TemplateView.as_view(
        template_name='index.css',
        content_type='text/css')
    ),
    path('admin/', admin.site.urls),
    path('', index, name='index')
]
