from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import permissions, status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.parsers import JSONParser
from django.utils import timezone
from .models import (
    Tablemate,
    PastWeekIntakes
)
from .serializers import (
    DemographicSerializer,
    TablemateSerializer,
    PastWeekIntakeBulkCreateSerializer,
    PastWeekIntakeSerializer,
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
        request_body=TablemateSerializer(many=True),
        responses={201: TablemateSerializer(many=True)},
    )
    def post(self, request, *args, **kwargs):

        serializer = TablemateSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)

        user = request.user

        tablemate_objects = []
        for item in serializer.validated_data:
            tablemate_objects.append(
                Tablemate(
                    user=user,
                    **item,
                )
            )

        created_tablemates = Tablemate.objects.bulk_create(tablemate_objects)

        output_serializer = TablemateSerializer(created_tablemates, many=True)
        return Response(output_serializer.data, status=status.HTTP_201_CREATED)

# ---------- 2) Submit endpoints (POST per form) ----------



class PastWeekIntakeTableCreateView(APIView):

    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [JSONParser]

    @swagger_auto_schema(
        operation_summary="ایجاد جدول مصرف هفتگی (تاریخ خودکار، آیتم‌ها به‌صورت آرایه)",
        request_body=PastWeekIntakeBulkCreateSerializer,
        responses={201: PastWeekIntakeSerializer(many=True)},
    )
    def post(self, request, *args, **kwargs):

        serializer = PastWeekIntakeBulkCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = request.user
        items = serializer.validated_data["items"]
        date = timezone.now().date()

        intake_objects = []
        for item in items:
            intake_objects.append(
                PastWeekIntakes(
                    user=user,
                    date=date,
                    **item,
                )
            )

        created_intakes = PastWeekIntakes.objects.bulk_create(intake_objects)

        output_serializer = PastWeekIntakeSerializer(created_intakes, many=True)
        return Response(output_serializer.data, status=status.HTTP_201_CREATED)
