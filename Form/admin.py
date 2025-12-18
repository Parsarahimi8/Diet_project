from django.contrib import admin
from .models import  PastWeekIntake,PreferrdFood,FreeShopping



@admin.register(PastWeekIntake)
class PWIAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "eggs", "dairy", "meat", "poultry",
        "honey", "fish", "olive", "sugar",
        "oilsM", "oilsS", "oilolive",
        "fruit", "vegetable", "nuts", "legumes",
        "potatoes", "stimuli", "rice", "barley", "wheat",
        "created_at",
    )
    list_filter = (
        "eggs", "dairy", "meat", "poultry",
        "honey", "fish", "olive", "sugar",
        "oilsM", "oilsS", "oilolive",
        "fruit", "vegetable", "nuts", "legumes",
        "potatoes", "stimuli", "rice", "barley", "wheat",
        "created_at",
    )
    search_fields = ()  # فیلد متنی خاصی نداری؛ اگر بعداً توضیح/کامنت متنی اضافه شد، اینجا اضافه کن.
    ordering = ("-created_at",)


@admin.register(PreferrdFood)
class PrFoodAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "Eggs", "Dairy", "Meat", "Poultry", "Honey", "Fish",
        "Olives", "Sugar", "OilsM", "OilsS", "Oil",
        "Fruit", "vegetables", "Nuts", "Legumes",
        "Potatoes", "Stimuli", "Rice", "Barley", "Wheat",
        "created_at", "updated_at",
    )
    list_filter = (
        "Eggs", "Dairy", "Meat", "Poultry", "Honey", "Fish",
        "Olives", "Sugar", "OilsM", "OilsS", "Oil",
        "Fruit", "vegetables", "Nuts", "Legumes",
        "Potatoes", "Stimuli", "Rice", "Barley", "Wheat",
        "created_at", "updated_at",
    )
    search_fields = ()  # اگر بعداً فیلد متنی قابل جست‌وجو اضافه شد، اینجا ست کنید.
    ordering = ("-created_at",)
    readonly_fields = ("created_at", "updated_at")
    date_hierarchy = "created_at"
    list_per_page = 50

@admin.register(FreeShopping)
class Form4Admin(admin.ModelAdmin):
    list_display = ("id", "created_at", "updated_at")

