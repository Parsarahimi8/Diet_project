from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import authenticate
from Form.serializers import (
    DemographicInformationFormSerializer,
    TablematesFormSerializer,
    PastWeekIntakeSerializer,
    PreferredFoodSerializer,
    FreeShoppingSerializer,
)


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'password']

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(email=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError("Invalid credentials")
        data['user'] = user
        return data
class VerifyOtpSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6)

class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6)
    new_password = serializers.CharField(min_length=6)


class UserProfileSerializer(serializers.ModelSerializer):
    # 🔹 همه‌ی فرم‌هایی که این یوزر ثبت کرده
    demographic_forms = DemographicInformationFormSerializer(many=True, read_only=True)
    tablemates = TablematesFormSerializer(many=True, read_only=True)
    past_week_intakes = PastWeekIntakeSerializer(many=True, read_only=True)
    preferred_foods = PreferredFoodSerializer(many=True, read_only=True)
    free_shoppings = FreeShoppingSerializer(many=True, read_only=True)

    class Meta:
        model = CustomUser
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "is_active",
            "is_staff",
            "last_login",

            # 🔽 این‌ها اضافه شدند:
            "demographic_forms",
            "tablemates",
            "past_week_intakes",
            "preferred_foods",
            "free_shoppings",
        ]
        read_only_fields = fields
