from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import  Tablemate, PastWeekIntakes, Category, FoodGroup
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
    sharedMealsCount = serializers.IntegerField(source="shared_meals_count")
    relationshipLevel = serializers.CharField(source="relationship_level", allow_blank=True, required=False)
    influenceLevel = serializers.CharField(source="influence_level", allow_blank=True, required=False)

    class Meta:
        model = Tablemate
        fields = [
            "id",
            "name",
            "sharedMealsCount",
            "relationshipLevel",
            "influenceLevel",
        ]
        read_only_fields = ["id"]


class TablemateBulkCreateSerializer(serializers.Serializer):
    tablemates = TablemateSerializer(many=True)

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

    class Meta:
        model = PastWeekIntakes
        fields = [
            "id",
            "user",
            "food_group",
            "value",
            "percent_usage",
            "created_at",
        ]
        read_only_fields = ["id", "user", "created_at"]



class FoodGroupNestedSerializer(serializers.ModelSerializer):
    categoryId = serializers.IntegerField(source="category_id", read_only=True)

    class Meta:
        model = FoodGroup
        fields = [
            "id",
            "code",
            "name",
            "title",
            "categoryId",
            "properties",
        ]


class CategoryWithFoodGroupsSerializer(serializers.ModelSerializer):
    foodGroups = FoodGroupNestedSerializer(source="food_groups", many=True, read_only=True)

    class Meta:
        model = Category
        fields = [
            "id",
            "name",
            "title",
            "properties",
            "foodGroups",
        ]