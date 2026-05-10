from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import  Tablemate, PastWeekIntakes, Category, FoodGroup, PreferredFood , FreeShopping, LimitedShopping, SocialAlignment
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
class PreferredFoodItemSerializer(serializers.ModelSerializer):
    food_group_id = serializers.PrimaryKeyRelatedField(
        queryset=FoodGroup.objects.all(),
        source="food_group"
    )

    class Meta:
        model = PreferredFood
        fields = [
            "food_group_id",
            "priority",
        ]
class PreferredFoodBulkCreateSerializer(serializers.Serializer):
    items = PreferredFoodItemSerializer(many=True)

class PreferredFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreferredFood
        fields = [
            "id",
            "user",
            "food_group",
            "priority",
        ]
        read_only_fields = ["id", "user"]


class FoodGroupListSerializer(serializers.ModelSerializer):

    class Meta:
        model = FoodGroup
        fields = [
            "id",
            "title",
            "code",
            "properties",
        ]



#################################################

class FreeShoppingItemSerializer(serializers.Serializer):
    food_group_id = serializers.PrimaryKeyRelatedField(
        queryset=FoodGroup.objects.all(),
        source="food_group"
    )
    value = serializers.FloatField()

class FreeShoppingBulkCreateSerializer(serializers.Serializer):
    items = FreeShoppingItemSerializer(many=True)

class FreeShoppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreeShopping
        fields = [
            "id",
            "user",
            "food_group",
            "value",
        ]
        read_only_fields = ["id", "user"]

class FreeShoppingSerializer(serializers.Serializer):
    id = serializers.IntegerField(source="food_group.id")
    title = serializers.CharField(source="food_group.title")
    value = serializers.IntegerField()


class LimitedShoppingItemSerializer(serializers.Serializer):
    food_group_id = serializers.PrimaryKeyRelatedField(
        queryset=FoodGroup.objects.all(),
        source="food_group"
    )
    value = serializers.FloatField()
    offset_price = serializers.FloatField()
    offset_health = serializers.FloatField()
    offset_environment = serializers.FloatField()

class LimitedShoppingBulkCreateSerializer(serializers.Serializer):
    items = LimitedShoppingItemSerializer(many=True)

class LimitedShoppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = LimitedShopping
        fields = [
            "id",
            "user",
            "food_group",
            "value",
            "offset_price",
            "offset_health",
            "offset_environment",
        ]
        read_only_fields = ["id", "user"]


class PreferredFoodListSerializer(serializers.Serializer):
    priority = serializers.IntegerField()
    food_group_id = serializers.IntegerField(source="food_group.id")
    food_group_title = serializers.CharField(source="food_group.title")



class SocialAlignmentCreateSerializer(serializers.Serializer):
    individualism_degree = serializers.FloatField()

class SocialAlignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialAlignment
        fields = ["id", "user", "individualism_degree"]
        read_only_fields = ["id", "user"]

