from rest_framework import serializers
from .models import DemographicForm, Form2, Form3, Form4

class DemographicFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = DemographicForm
        fields = [
            "id",
            "name", "age", "gender",
            "height_cm", "weight_kg",
            "education",
            "job_state",
            "income_bracket",
            "diet_income_percent",
            "province",
            "marital_status",
            "family_members",
            "sport_days_per_week",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]

class Form2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Form2
        fields = ["id", "title", "data", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]

class Form3Serializer(serializers.ModelSerializer):
    class Meta:
        model = Form3
        fields = ["id", "title", "data", "is_active", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]

class Form4Serializer(serializers.ModelSerializer):
    class Meta:
        model = Form4
        fields = ["id", "title", "notes", "data", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]
