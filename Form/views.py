from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import permissions, status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import (
    DemographicFormInformation,
    Tablemates,
    PastWeekIntake,
    PreferrdFood,
    FreeShopping,
)
from .serializers import (
    DemographicInformationFormSerializer,
    TablematesFormSerializer,
    PastWeekIntakeSerializer,
    PreferredFoodSerializer,
    FreeShoppingSerializer,
)


# ---------- 1) Catalog (GET) ----------
class FormsCatalogView(APIView):
    """
    لیست چهار فرم موجود: عنوان، توضیح، endpoint ارسال (POST).
    """
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(
        operation_summary="دریافت فهرست فرم‌ها",
        operation_description="چهار فرم فعال را با عنوان و آدرس POST بازمی‌گرداند.",
        responses={200: openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "forms": openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Items(type=openapi.TYPE_OBJECT, properties={
                        "key": openapi.Schema(type=openapi.TYPE_STRING, description="شناسه‌ی کوتاه فرم"),
                        "title": openapi.Schema(type=openapi.TYPE_STRING),
                        "description": openapi.Schema(type=openapi.TYPE_STRING),
                        "endpoint": openapi.Schema(type=openapi.TYPE_STRING, description="مسیر POST این فرم"),
                        "method": openapi.Schema(type=openapi.TYPE_STRING, default="POST"),
                    })
                )
            }
        )}
    )
    def get(self, request):
        base = "/api/forms"  # ریشه‌ی این اپ در پروژه
        data = {
            "forms": [
                {
                    "key": "form1",
                    "title": "فرم دموگرافیک",
                    "description": "اطلاعات پایه: سن، جنسیت، قد/وزن، تحصیلات، شغل، درآمد، استان، تاهل، اعضای خانواده، ورزش.",
                    "endpoint": f"{base}/form1/",
                    "method": "POST",
                },
                {
                    "key": "form2",
                    "title": "فرم ۲ (سادۀ قابل گسترش)",
                    "description": "ساختار آزاد با JSON برای توسعه‌های بعدی.",
                    "endpoint": f"{base}/form2/",
                    "method": "POST",
                },
                {
                    "key": "form3",
                    "title": "فرم ۳ (سادۀ قابل گسترش)",
                    "description": "شامل فیلد is_active برای سناریوهای وضعیت‌دار.",
                    "endpoint": f"{base}/form3/",
                    "method": "POST",
                },
                {
                    "key": "form4",
                    "title": "فرم ۴ (سادۀ قابل گسترش)",
                    "description": "دارای notes و JSON برای انعطاف بالا.",
                    "endpoint": f"{base}/form4/",
                    "method": "POST",
                },
            ]
        }
        return Response(data, status=status.HTTP_200_OK)


# ---------- 2) Submit endpoints (POST per form) ----------

class DemographicFormCreateView(CreateAPIView):
    """
    ایجاد پاسخ جدید برای فرم دموگرافیک (Form1).
    (مرحله اول، بدون پیش‌نیاز)
    """
    permission_classes = [permissions.AllowAny]
    queryset = DemographicFormInformation.objects.all()
    serializer_class = DemographicInformationFormSerializer

    @swagger_auto_schema(
        operation_summary="ارسال فرم دموگرافیک (Form1)",
        request_body=DemographicInformationFormSerializer,
        responses={201: DemographicInformationFormSerializer}
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class MiddleFormCreateView(CreateAPIView):
    """
    ایجاد رکورد جدید MiddleForm (تکی یا چندتایی)
    مرحله دوم:
      فقط اگر فرم دموگرافیک (Form1) قبلاً برای این user ثبت شده باشد.
    """
    permission_classes = [permissions.AllowAny]
    queryset = Tablemates.objects.all()
    serializer_class = TablematesFormSerializer

    @swagger_auto_schema(
        operation_summary="افزودن همسفره (تکی یا چندتایی)",
        operation_description=(
            "می‌تواند یک آبجکت یا آرایه‌ای از آبجکت‌ها دریافت کند.\n\n"
            "ساختار هر آبجکت:\n"
            "{name: string, shared_meals_count: number, relationship_level: string, influence_level: string}\n\n"
            "**Choices**\n"
            "- shared_meals_count: 1 | 2 | 3 | 4 | 5\n"
            "- relationship_level: family | friend | colleague | other\n"
            "- influence_level: none | low | medium | high | very_high\n"
        ),
        request_body=TablematesFormSerializer(many=True),
        responses={201: TablematesFormSerializer(many=True)},
    )
    def post(self, request, *args, **kwargs):
        data = request.data

        # 🔹 user id را از داده (تکی یا لیستی) بگیر
        if isinstance(data, list):
            if not data:
                return Response(
                    {"detail": "لیست داده خالی است."},
                    status=status.HTTP_400_BAD_REQUEST
                )
            user_id = data[0].get("user")
        else:
            user_id = data.get("user")

        if not user_id:
            return Response(
                {"detail": "فیلد user الزامی است."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # 🔹 مرحله ۲ فقط درصورتی مجاز است که فرم دموگرافیک وجود داشته باشد
        if not DemographicFormInformation.objects.filter(user_id=user_id).exists():
            return Response(
                {"detail": "ابتدا باید فرم دموگرافیک (Form1) را تکمیل کنید."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # ادامهٔ منطق قبلی
        is_many = isinstance(data, list)

        serializer = self.get_serializer(data=data, many=is_many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        if is_many:
            first_item = serializer.data[0] if serializer.data else None
            headers = self.get_success_headers(first_item) if first_item else {}
        else:
            headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class PWIFormCreateView(CreateAPIView):
    """
    ایجاد پاسخ جدید برای فرم تغذیه (Form2 - PWI).
    مرحله سوم:
      فقط اگر:
        1) فرم دموگرافیک (Form1)
        2) فرم همسفره‌ها / MiddleForm (Form2)
      قبلاً برای این user ثبت شده باشند.
    """
    permission_classes = [permissions.AllowAny]
    queryset = PastWeekIntake.objects.all()
    serializer_class = PastWeekIntakeSerializer

    @swagger_auto_schema(
        operation_summary="ارسال فرم تغذیه (Form3 - PWI)",
        request_body=PastWeekIntakeSerializer,
        responses={201: PastWeekIntakeSerializer}
    )
    def post(self, request, *args, **kwargs):
        user_id = request.data.get("user")

        if not user_id:
            return Response(
                {"detail": "فیلد user الزامی است."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # ۱) باید فرم دموگرافیک داشته باشد
        if not DemographicFormInformation.objects.filter(user_id=user_id).exists():
            return Response(
                {"detail": "ابتدا باید فرم دموگرافیک (Form1) را تکمیل کنید."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # ۲) باید حداقل یک MiddleForm داشته باشد
        if not Tablemates.objects.filter(user_id=user_id).exists():
            return Response(
                {"detail": "ابتدا باید فرم همسفره‌ها (Form2) را تکمیل کنید."},
                status=status.HTTP_400_BAD_REQUEST
            )

        return super().post(request, *args, **kwargs)


class PrFoodCreateView(CreateAPIView):
    """
    ایجاد پاسخ جدید برای فرم ترجیحات غذایی (Form5 - PrFood).
    مرحله چهارم:
      فقط اگر:
        1) فرم دموگرافیک (Form1)
        2) MiddleForm (Form2)
        3) PastWeekIntake (Form3)
      قبلاً برای این user ثبت شده باشند.
    """
    permission_classes = [permissions.AllowAny]
    queryset = PreferrdFood.objects.all()
    serializer_class = PreferredFoodSerializer

    @swagger_auto_schema(
        operation_summary="ارسال فرم ترجیحات غذایی (Form4 - PrFood)",
        request_body=PreferredFoodSerializer,
        responses={201: PreferredFoodSerializer}
    )
    def post(self, request, *args, **kwargs):
        user_id = request.data.get("user")

        if not user_id:
            return Response(
                {"detail": "فیلد user الزامی است."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # ۱) فرم دموگرافیک
        if not DemographicFormInformation.objects.filter(user_id=user_id).exists():
            return Response(
                {"detail": "ابتدا باید فرم دموگرافیک (Form1) را تکمیل کنید."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # ۲) MiddleForm
        if not Tablemates.objects.filter(user_id=user_id).exists():
            return Response(
                {"detail": "ابتدا باید فرم همسفره‌ها (Form2) را تکمیل کنید."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # ۳) PastWeekIntake
        if not PastWeekIntake.objects.filter(user_id=user_id).exists():
            return Response(
                {"detail": "ابتدا باید فرم تغذیه هفتگی (Form3 - PWI) را تکمیل کنید."},
                status=status.HTTP_400_BAD_REQUEST
            )

        return super().post(request, *args, **kwargs)


class FreeShoppingView(CreateAPIView):
    """
    ایجاد پاسخ جدید برای فرم خرید آزاد (Form5 - FreeShopping).
    مرحله پنجم (آخر):
      فقط اگر:
        1) فرم دموگرافیک (Form1)
        2) MiddleForm (Form2)
        3) PastWeekIntake (Form3)
        4) PreferredFood (Form4)
      قبلاً برای این user ثبت شده باشند.
    """
    permission_classes = [permissions.AllowAny]
    queryset = FreeShopping.objects.all()
    serializer_class = FreeShoppingSerializer

    @swagger_auto_schema(
        operation_summary="ارسال فرم ۵ (FreeShopping)",
        request_body=FreeShoppingSerializer,
        responses={201: FreeShoppingSerializer}
    )
    def post(self, request, *args, **kwargs):
        user_id = request.data.get("user")

        if not user_id:
            return Response(
                {"detail": "فیلد user الزامی است."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # ۱) فرم دموگرافیک
        if not DemographicFormInformation.objects.filter(user_id=user_id).exists():
            return Response(
                {"detail": "ابتدا باید فرم دموگرافیک (Form1) را تکمیل کنید."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # ۲) MiddleForm
        if not Tablemates.objects.filter(user_id=user_id).exists():
            return Response(
                {"detail": "ابتدا باید فرم همسفره‌ها (Form2) را تکمیل کنید."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # ۳) PastWeekIntake
        if not PastWeekIntake.objects.filter(user_id=user_id).exists():
            return Response(
                {"detail": "ابتدا باید فرم تغذیه هفتگی (Form3 - PWI) را تکمیل کنید."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # ۴) PreferredFood
        if not PreferrdFood.objects.filter(user_id=user_id).exists():
            return Response(
                {"detail": "ابتدا باید فرم ترجیحات غذایی (Form4 - PreferredFood) را تکمیل کنید."},
                status=status.HTTP_400_BAD_REQUEST
            )

        return super().post(request, *args, **kwargs)
