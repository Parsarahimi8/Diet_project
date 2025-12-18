from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import  Tablemate, PastWeekIntakes
from users.models import  CustomUser
User = get_user_model()


class DemographicSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "id",
            "email",
            "full_name",
            "age",
            "gender",
            "properties",
        ]
        read_only_fields = ["id"]

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)



class TablemateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tablemate
        fields = [
            "id",
            "name",
            "shared_meals_count",
            "relationship_level",
            "influence_level",
        ]
        read_only_fields = ["id"]



class PastWeekIntakeItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PastWeekIntakes
        fields = [
            "food_group",
            "value",
            "percent_usage",
        ]


class PastWeekIntakeBulkCreateSerializer(serializers.Serializer):

    items = PastWeekIntakeItemSerializer(many=True)

class PastWeekIntakeSerializer(serializers.ModelSerializer):
    """
    خروجی نهایی برای هر ردیف PastWeekIntake.
    """
    class Meta:
        model = PastWeekIntakes
        fields = [
            "id",
            "user",
            "food_group",
            "value",
            "percent_usage",
            "date",
        ]
        read_only_fields = ["id", "user", "date"]