from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import PastWeekIntake, PreferrdFood, FreeShopping,Tablemate
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


# برای categoryName
CATEGORY_CHOICES = [
    ("Protein", "Protein"),
    ("Stimuli&Sweet", "Stimuli&Sweet"),
    ("Oils", "Oils"),
    ("carbohydrates", "carbohydrates"),
    ("fiber&vitamin", "fiber&vitamin"),
    ("Combinations", "Combinations"),
]


class FoodItemSerializer(serializers.Serializer):
    value = serializers.CharField()
    percentUsage = serializers.CharField()
    categoryName = serializers.ChoiceField(choices=CATEGORY_CHOICES)

    def to_representation(self, instance):
        score = instance.get("score")
        percent = instance.get("percentUsage")
        cat = instance.get("categoryName")

        return {
            "value": score,
            "percentUsage": percent,
            "categoryName": cat,
        }


class PastWeekIntakeSerializer(serializers.ModelSerializer):
    # ✅ user id
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    eggs = FoodItemSerializer()
    dairy = FoodItemSerializer()
    meat = FoodItemSerializer()
    poultry = FoodItemSerializer()
    honey = FoodItemSerializer()
    fish = FoodItemSerializer()
    olive = FoodItemSerializer()
    sugar = FoodItemSerializer()
    oilsM = FoodItemSerializer()
    oilsS = FoodItemSerializer()
    oilolive = FoodItemSerializer()
    fruit = FoodItemSerializer()
    vegetable = FoodItemSerializer()
    nuts = FoodItemSerializer()
    legumes = FoodItemSerializer()
    potatoes = FoodItemSerializer()
    stimuli = FoodItemSerializer()
    rice = FoodItemSerializer()
    barley = FoodItemSerializer()
    wheat = FoodItemSerializer()

    class Meta:
        model = PastWeekIntake
        fields = [
            "id",
            "user",   # ✅
            "eggs", "dairy", "meat", "poultry",
            "honey", "fish", "olive", "sugar",
            "oilsM", "oilsS", "oilolive",
            "fruit", "vegetable", "nuts", "legumes",
            "potatoes", "stimuli", "rice", "barley", "wheat",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]

    FOOD_CHOICE_MAP = {
        "eggs": PastWeekIntake.Eggs.choices,
        "dairy": PastWeekIntake.Dairy.choices,
        "meat": PastWeekIntake.Meat.choices,
        "poultry": PastWeekIntake.Poultry.choices,
        "honey": PastWeekIntake.Honey.choices,
        "fish": PastWeekIntake.Fish.choices,
        "olive": PastWeekIntake.Olive.choices,
        "sugar": PastWeekIntake.Sugar.choices,
        "oilsM": PastWeekIntake.OilsM.choices,
        "oilsS": PastWeekIntake.OilsS.choices,
        "oilolive": PastWeekIntake.OilOlive.choices,
        "fruit": PastWeekIntake.Fruit.choices,
        "vegetable": PastWeekIntake.Vegetables.choices,
        "nuts": PastWeekIntake.Nuts.choices,
        "legumes": PastWeekIntake.Legumes.choices,
        "potatoes": PastWeekIntake.Potatoes.choices,
        "stimuli": PastWeekIntake.Stimuli.choices,
        "rice": PastWeekIntake.Rice.choices,
        "barley": PastWeekIntake.Barley.choices,
        "wheat": PastWeekIntake.Wheat.choices,
    }

    def validate(self, attrs):
        for field, choices in self.FOOD_CHOICE_MAP.items():
            item = attrs.get(field)
            if item is None:
                continue

            raw_value = item["value"]
            choices_map = dict(choices)

            if raw_value not in choices_map:
                raise serializers.ValidationError(
                    {
                        field: f"مقدار نامعتبر. مقادیر مجاز: {list(choices_map.keys())}"
                    }
                )

            score = choices_map[raw_value]

            attrs[field] = {
                "score": score,
                "percentUsage": item["percentUsage"],
                "categoryName": item["categoryName"],
            }

        return attrs


class PreferredFoodSerializer(serializers.ModelSerializer):
    # ✅ user id
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = PreferrdFood
        fields = [
            "id",
            "user",   # ✅
            "Eggs", "Dairy", "Meat", "Poultry", "Honey", "Fish",
            "Olives", "Sugar", "OilsM", "OilsS", "Oil",
            "Fruit", "vegetables", "Nuts", "Legumes",
            "Potatoes", "Stimuli", "Rice", "Barley", "Wheat",
            "created_at", "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]


class FreeShoppingSerializer(serializers.ModelSerializer):
    # ✅ user id
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = FreeShopping
        fields = [
            "id",
            "user",   # ✅
            "Eggs", "Dairy", "Meat", "Poultry", "Honey", "Fish",
            "Olives", "Sugar", "OilsM", "OilsS", "Oil",
            "Fruit", "vegetables", "Nuts", "Legumes",
            "Potatoes", "Stimuli", "Rice", "Barley", "Wheat",
            "created_at", "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
