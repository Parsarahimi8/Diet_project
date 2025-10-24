from rest_framework import viewsets, permissions, filters
from .models import News, Diet, Podcast, Paper, About
from .serializers import (
    NewsSerializer, DietSerializer, PodcastSerializer, PaperSerializer, AboutSerializer
)

class ReadOnlyOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in ("GET", "HEAD", "OPTIONS"):
            return True
        return bool(request.user and request.user.is_staff)

class BaseViewSet(viewsets.ModelViewSet):
    permission_classes = [ReadOnlyOrAdmin]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ["created_at", "updated_at"]

class NewsViewSet(BaseViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    search_fields = ["title", "summary", "body"]
    ordering_fields = ["published_at", "created_at"]

class DietViewSet(BaseViewSet):
    queryset = Diet.objects.all()
    serializer_class = DietSerializer
    search_fields = ["name", "description", "tags"]

class PodcastViewSet(BaseViewSet):
    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializer
    search_fields = ["title", "description"]
    ordering_fields = ["published_at", "created_at", "duration_seconds"]

class PaperViewSet(BaseViewSet):
    queryset = Paper.objects.all()
    serializer_class = PaperSerializer
    search_fields = ["title", "abstract", "source_name", "paper_type"]
    ordering_fields = ["published_at", "created_at"]

class AboutViewSet(BaseViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
    search_fields = ["heading", "body", "contact_email", "contact_phone"]
