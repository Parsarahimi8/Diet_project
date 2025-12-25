from django.contrib import admin
from .models import Tablemate, PastWeekIntakes,FoodGroup,Category



@admin.register(Tablemate)
class TablemateAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "user",
        "shared_meals_count",
        "relationship_level",
        "influence_level",
    )
    list_filter = (
        "relationship_level",
        "influence_level",
    )
    search_fields = (
        "name",
        "user__email",
        "user__full_name",
    )
    raw_id_fields = ("user",)
    ordering = ("id",)



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "title")
    search_fields = ("name", "title")
    ordering = ("id",)


@admin.register(FoodGroup)
class FoodGroupAdmin(admin.ModelAdmin):
    list_display = ("id", "code", "name", "title", "category")
    list_filter = ("category",)
    search_fields = ("name", "title", "code")
    raw_id_fields = ("category",)
    ordering = ("id",)

@admin.register(PastWeekIntakes)
class PastWeekIntakesAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "food_group",
        "value",
        "percent_usage",
        "created_at",
    )
    list_filter = ("food_group", "created_at")
    search_fields = ("user__email", "user__full_name", "food_group__title")
    raw_id_fields = ("user", "food_group")
    ordering = ("-created_at",)

