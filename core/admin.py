from django.contrib import admin
from .models import News, Diet, Podcast, Paper, About
admin.site.register([News, Diet, Podcast, Paper, About])
