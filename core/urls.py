from django.urls import path
from .views import (
    NewsListAPI, NewsDetailAPI,
    DietListAPI, DietDetailAPI,
    PodcastListAPI, PodcastDetailAPI,
    PaperListAPI, PaperDetailAPI,
    AboutListAPI, AboutDetailAPI,
)

urlpatterns = [
    path("news/", NewsListAPI.as_view(), name="news-list"),
    path("news/<int:pk>/", NewsDetailAPI.as_view(), name="news-detail"),

    path("diets/", DietListAPI.as_view(), name="diet-list"),
    path("diets/<int:pk>/", DietDetailAPI.as_view(), name="diet-detail"),

    path("podcasts/", PodcastListAPI.as_view(), name="podcast-list"),
    path("podcasts/<int:pk>/", PodcastDetailAPI.as_view(), name="podcast-detail"),

    path("papers/", PaperListAPI.as_view(), name="paper-list"),
    path("papers/<int:pk>/", PaperDetailAPI.as_view(), name="paper-detail"),

    path("about/", AboutListAPI.as_view(), name="about-list"),
    path("about/<int:pk>/", AboutDetailAPI.as_view(), name="about-detail"),
]
