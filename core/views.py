from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.shortcuts import get_object_or_404

from .models import News, Diet, Podcast, Paper, About
from .serializers import (
    NewsSerializer, DietSerializer, PodcastSerializer, PaperSerializer, AboutSerializer
)

# ---- NEWS ----
class NewsListAPI(APIView):
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(responses={200: NewsSerializer(many=True)})
    def get(self, request):
        qs = News.objects.filter(is_published=True)
        return Response(NewsSerializer(qs, many=True).data, status=status.HTTP_200_OK)

class NewsDetailAPI(APIView):
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(responses={200: NewsSerializer()})
    def get(self, request, pk: int):
        obj = get_object_or_404(News, pk=pk, is_published=True)
        return Response(NewsSerializer(obj).data, status=status.HTTP_200_OK)

# ---- DIET ----
class DietListAPI(APIView):
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(responses={200: DietSerializer(many=True)})
    def get(self, request):
        qs = Diet.objects.all()
        return Response(DietSerializer(qs, many=True).data, status=status.HTTP_200_OK)

class DietDetailAPI(APIView):
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(responses={200: DietSerializer()})
    def get(self, request, pk: int):
        obj = get_object_or_404(Diet, pk=pk)
        return Response(DietSerializer(obj).data, status=status.HTTP_200_OK)

# ---- PODCAST ----
class PodcastListAPI(APIView):
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(responses={200: PodcastSerializer(many=True)})
    def get(self, request):
        qs = Podcast.objects.filter(is_published=True)
        return Response(PodcastSerializer(qs, many=True).data, status=status.HTTP_200_OK)

class PodcastDetailAPI(APIView):
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(responses={200: PodcastSerializer()})
    def get(self, request, pk: int):
        obj = get_object_or_404(Podcast, pk=pk, is_published=True)
        return Response(PodcastSerializer(obj).data, status=status.HTTP_200_OK)

# ---- PAPER ----
class PaperListAPI(APIView):
    permission_classes = [permissions.AllowAny]

    type_param = openapi.Parameter(
        "type", openapi.IN_QUERY, type=openapi.TYPE_STRING,
        enum=["data", "journal"], description="Filter by paper_type"
    )

    @swagger_auto_schema(manual_parameters=[type_param], responses={200: PaperSerializer(many=True)})
    def get(self, request):
        qs = Paper.objects.all()
        t = request.query_params.get("type")
        if t in {"data", "journal"}:
            qs = qs.filter(paper_type=t)
        return Response(PaperSerializer(qs, many=True).data, status=status.HTTP_200_OK)

class PaperDetailAPI(APIView):
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(responses={200: PaperSerializer()})
    def get(self, request, pk: int):
        obj = get_object_or_404(Paper, pk=pk)
        return Response(PaperSerializer(obj).data, status=status.HTTP_200_OK)

# ---- ABOUT ----
class AboutListAPI(APIView):
    """
    If you only want ONE About record, just create one in admin and use the first() in detail view.
    Keeping list for flexibility.
    """
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(responses={200: AboutSerializer(many=True)})
    def get(self, request):
        qs = About.objects.all()
        return Response(AboutSerializer(qs, many=True).data, status=status.HTTP_200_OK)

class AboutDetailAPI(APIView):
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(responses={200: AboutSerializer()})
    def get(self, request, pk: int):
        obj = get_object_or_404(About, pk=pk)
        return Response(AboutSerializer(obj).data, status=status.HTTP_200_OK)

