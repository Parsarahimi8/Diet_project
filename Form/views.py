from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import JSONParser
from django.db import transaction


from .models import Tablemate, PastWeekIntakes, Category
from .serializers import (
    DemographicSerializer,
    TablemateBulkCreateSerializer, TablemateSerializer,
    PastWeekIntakeBulkCreateSerializer,
    PastWeekIntakeSerializer,
    CategoryWithFoodGroupsSerializer
)


class DemographicView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

    @swagger_auto_schema(
        operation_summary="دریافت پروفایل کاربر لاگین‌شده",
        responses={200: DemographicSerializer},
    )
    def get(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = DemographicSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_summary="ویرایش پروفایل کاربر لاگین‌شده",
        request_body=DemographicSerializer,
        responses={200: DemographicSerializer},
    )
    def put(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = DemographicSerializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

class TablemateView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [JSONParser]

    @swagger_auto_schema(
        operation_summary="ایجاد هم‌سفره‌ها برای کاربر لاگین‌شده",
        request_body=TablemateBulkCreateSerializer,
        responses={201: TablemateSerializer(many=True)},
    )
    def post(self, request, *args, **kwargs):
        serializer = TablemateBulkCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = request.user
        items = serializer.validated_data["tablemates"]

        tablemate_objects = [Tablemate(user=user, **item) for item in items]
        created_tablemates = Tablemate.objects.bulk_create(tablemate_objects)

        output_serializer = TablemateSerializer(created_tablemates, many=True)
        return Response(output_serializer.data, status=status.HTTP_201_CREATED)


class PastWeekIntakeTableCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [JSONParser]

    @swagger_auto_schema(
        operation_summary="ایجاد جدول مصرف هفتگی (created_at خودکار، آیتم‌ها به‌صورت آرایه)",
        request_body=PastWeekIntakeBulkCreateSerializer,
        responses={201: PastWeekIntakeSerializer(many=True)},
    )
    def post(self, request, *args, **kwargs):
        serializer = PastWeekIntakeBulkCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = request.user
        items = serializer.validated_data["items"]

        intake_objects = [
            PastWeekIntakes(user=user, **item)
            for item in items
        ]

        created_intakes = PastWeekIntakes.objects.bulk_create(intake_objects)

        output_serializer = PastWeekIntakeSerializer(created_intakes, many=True)
        return Response(output_serializer.data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        operation_summary="ویرایش جدول مصرف هفتگی (آپدیت/ایجاد بر اساس food_group برای کاربر لاگین‌شده)",
        request_body=PastWeekIntakeBulkCreateSerializer,
        responses={200: PastWeekIntakeSerializer(many=True)},
    )
    def put(self, request, *args, **kwargs):
        serializer = PastWeekIntakeBulkCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = request.user
        items = serializer.validated_data["items"]

        updated_or_created = []

        with transaction.atomic():
            for item in items:
                food_group = item["food_group"]
                value = item["value"]
                percent_usage = item.get("percent_usage")

                obj = (
                    PastWeekIntakes.objects
                        .filter(user=user, food_group=food_group)
                        .order_by("-created_at")
                        .first()
                )

                if obj:
                    obj.value = value
                    obj.percent_usage = percent_usage
                    obj.save(update_fields=["value", "percent_usage"])
                    updated_or_created.append(obj)
                else:
                    new_obj = PastWeekIntakes.objects.create(
                        user=user,
                        food_group=food_group,
                        value=value,
                        percent_usage=percent_usage,
                    )
                    updated_or_created.append(new_obj)

        output_serializer = PastWeekIntakeSerializer(updated_or_created, many=True)
        return Response(output_serializer.data, status=status.HTTP_200_OK)



class CategoryFoodGroupListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="لیست Category به همراه FoodGroupهای زیرمجموعه",
        responses={200: CategoryWithFoodGroupsSerializer(many=True)},
    )
    def get(self, request, *args, **kwargs):
        qs = (
            Category.objects
            .prefetch_related("food_groups")
            .all()
            .order_by("id")
        )
        serializer = CategoryWithFoodGroupsSerializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.parsers import JSONParser
from drf_yasg.utils import swagger_auto_schema

from .models import PreferredFood
from .serializers import PreferredFoodBulkCreateSerializer, PreferredFoodSerializer


class PreferredFoodTableCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [JSONParser]

    @swagger_auto_schema(
        operation_summary="ایجاد PreferredFood (آیتم‌ها به‌صورت آرایه)",
        request_body=PreferredFoodBulkCreateSerializer,
        responses={201: PreferredFoodSerializer(many=True)},
    )
    def post(self, request, *args, **kwargs):
        serializer = PreferredFoodBulkCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = request.user
        items = serializer.validated_data["items"]

        preferred_objects = [
            PreferredFood(user=user, **item)
            for item in items
        ]

        created = PreferredFood.objects.bulk_create(preferred_objects)

        output = PreferredFoodSerializer(created, many=True)
        return Response(output.data, status=status.HTTP_201_CREATED)
