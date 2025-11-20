from rest_framework import serializers
from .models import DemographicForm,  Form3, Form4, MiddleForm,PWI

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

class PWISerializer(serializers.ModelSerializer):
    class Meta:
        model = PWI
        fields = [
            "id",
            "eggs", "dairy", "meat", "poultry",
            "honey", "fish", "olive", "sugar",
            "oilsM", "oilsS", "oilolive",
            "fruit", "vegetable", "nuts", "legumes",
            "potatoes", "stimuli", "rice", "barley", "wheat",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]



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


class MiddleFormSerializer(serializers.ModelSerializer):
    """
    فیلدها و مقادیر مجاز (choices):
      - shared_meals_count: 1 | 2 | 3 | 4 | 5
      - relationship_level: family | friend | colleague | other
      - influence_level: none | low | medium | high | very_high
    """
    class Meta:
        model = MiddleForm
        fields = [
            "id",
            "name",
            "shared_meals_count",
            "relationship_level",
            "influence_level",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
        extra_kwargs = {
            "shared_meals_count": {
                "help_text": "یکی از اعداد 1 تا 5 (تعداد وعده مشترک)",
            },
            "relationship_level": {
                "help_text": "یکی از: family, friend, colleague, other",
            },
            "influence_level": {
                "help_text": "یکی از: none, low, medium, high, very_high",
            },
        }



