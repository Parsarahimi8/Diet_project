from django.urls import path
from .views import (
    DemographicView,
    TablemateView,
    PastWeekIntakeTableCreateView,
    CategoryFoodGroupListView,
    PreferredFoodTableCreateView,
    FoodGroupListView,
    FreeShoppingCreateView,
    FreeShoppingListView,
    LimitedShoppingCreateView,
    PreferredFoodListView
    )

app_name = "form"

urlpatterns = [
    path("forms/form1/", DemographicView.as_view(), name="form1"),
    path("forms/form2/", TablemateView.as_view(), name="form2"),
    path("forms/form3/", PastWeekIntakeTableCreateView.as_view(), name="form3"),
    path("forms/form4/", CategoryFoodGroupListView.as_view(), name="form4"),
    path("forms/form5/", PreferredFoodTableCreateView.as_view(), name="form5"),
    path("forms/form6/", FoodGroupListView.as_view(), name="form6"),
    path("forms/form7/", FreeShoppingCreateView.as_view(), name="freeshopping-create"),
    path("forms/form8/", FreeShoppingListView.as_view(), name="freeshopping-list"),
    path("forms/form9/", LimitedShoppingCreateView.as_view(), name="limitedshopping-create"),
    path("forms/form10/", PreferredFoodListView.as_view(), name="preferredfood-list"),




]

