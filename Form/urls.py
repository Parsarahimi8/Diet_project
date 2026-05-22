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
    PreferredFoodListView,
    SocialAlignmentCreateView
)

app_name = "form"

urlpatterns = [
    # --- Demographic ---
    path("demographic/", DemographicView.as_view(), name="demographic"),

    # --- Tablemate ---
    path("tablemate/", TablemateView.as_view(), name="tablemate"),

    # --- Intake ---
    path("intake/past-week/", PastWeekIntakeTableCreateView.as_view(), name="past-week-intake"),

    # --- Food Categories & Groups ---
    path("food/categories/", CategoryFoodGroupListView.as_view(), name="category-food-list"),
    path("food/groups/", FoodGroupListView.as_view(), name="food-group-list"),
    path("food/preferred/", PreferredFoodTableCreateView.as_view(), name="preferred-food-create"),
    path("food/preferred/list/", PreferredFoodListView.as_view(), name="preferred-food-list"),

    # --- Shopping ---
    path("shopping/free/create/", FreeShoppingCreateView.as_view(), name="free-shopping-create"),
    path("shopping/free/list/", FreeShoppingListView.as_view(), name="free-shopping-list"),
    path("shopping/limited/create/", LimitedShoppingCreateView.as_view(), name="limited-shopping-create"),

    # --- Social ---
    path("social/alignment/", SocialAlignmentCreateView.as_view(), name="social-alignment"),
]
