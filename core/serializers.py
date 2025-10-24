from rest_framework import serializers
from .models import News, Diet, Podcast, Paper, About

class NewsSerializer(serializers.ModelSerializer):
    class Meta: model = News; fields = "__all__"

class DietSerializer(serializers.ModelSerializer):
    class Meta: model = Diet; fields = "__all__"

class PodcastSerializer(serializers.ModelSerializer):
    class Meta: model = Podcast; fields = "__all__"

class PaperSerializer(serializers.ModelSerializer):
    class Meta: model = Paper; fields = "__all__"

class AboutSerializer(serializers.ModelSerializer):
    class Meta: model = About; fields = "__all__"
