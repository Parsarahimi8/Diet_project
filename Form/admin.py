from django.contrib import admin
from .models import DemographicForm,Form2,Form3,Form4,MiddleForm

@admin.register(DemographicForm)
class DemographicFormAdmin(admin.ModelAdmin):
    list_display = ("name", "age", "gender", "province", "job_state", "income_bracket", "created_at")
    list_filter = ("gender", "province", "job_state", "income_bracket", "marital_status", "sport_days_per_week")
    search_fields = ("name", "education")

@admin.register(Form2)
class Form2Admin(admin.ModelAdmin):
    list_display = ("id", "title", "created_at", "updated_at")
    search_fields = ("title",)

@admin.register(Form3)
class Form3Admin(admin.ModelAdmin):
    list_display = ("id", "title", "is_active", "created_at", "updated_at")
    list_filter = ("is_active",)
    search_fields = ("title",)

@admin.register(Form4)
class Form4Admin(admin.ModelAdmin):
    list_display = ("id", "title", "created_at", "updated_at")
    search_fields = ("title",)

@admin.register(MiddleForm)
class MiddleFormAdmin(admin.ModelAdmin):
    list_display = ("id","name", "shared_meals_count", "relationship_level", "influence_level", "created_at")
    list_filter = ("shared_meals_count", "relationship_level", "influence_level")
    ordering = ("-created_at",)