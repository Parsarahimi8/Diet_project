from rest_framework import serializers
from .models import DemographicFormInformation, Tablemates,PastWeekIntake, PreferrdFood, FreeShopping

class DemographicInformationFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = DemographicFormInformation
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




class TablematesFormSerializer(serializers.ModelSerializer):
    """
    فیلدها و مقادیر مجاز (choices):
      - shared_meals_count: 1 | 2 | 3 | 4 | 5
      - relationship_level: family | friend | colleague | other
      - influence_level: none | low | medium | high | very_high
    """
    class Meta:
        model = Tablemates
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


class PastWeekIntakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PastWeekIntake
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


class PreferredFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreferrdFood
        fields = [
            "id",
            "Eggs", "Dairy", "Meat", "Poultry", "Honey", "Fish",
            "Olives", "Sugar", "OilsM", "OilsS", "Oil",
            "Fruit", "vegetables", "Nuts", "Legumes",
            "Potatoes", "Stimuli", "Rice", "Barley", "Wheat",
            "created_at", "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]



class FreeShoppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreeShopping
        fields = [
            "id",
            "Eggs", "Dairy", "Meat", "Poultry", "Honey", "Fish",
            "Olives", "Sugar", "OilsM", "OilsS", "Oil",
            "Fruit", "vegetables", "Nuts", "Legumes",
            "Potatoes", "Stimuli", "Rice", "Barley", "Wheat",
            "created_at", "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]





