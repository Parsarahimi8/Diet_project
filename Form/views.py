from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import permissions, status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import DemographicForm, Form3, Form4,MiddleForm ,PWI
from .serializers import (
    DemographicFormSerializer,
     Form3Serializer, Form4Serializer,MiddleFormSerializer,PWISerializer
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
    """
    permission_classes = [permissions.AllowAny]
    queryset = DemographicForm.objects.all()
    serializer_class = DemographicFormSerializer

    @swagger_auto_schema(
        operation_summary="ارسال فرم دموگرافیک (Form1)",
        request_body=DemographicFormSerializer,
        responses={201: DemographicFormSerializer}
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)




class Form2CreateView(CreateAPIView):
    """
    ایجاد پاسخ جدید برای فرم تغذیه (Form2 - PWI).
    """
    permission_classes = [permissions.AllowAny]
    queryset = PWI.objects.all()
    serializer_class = PWISerializer

    @swagger_auto_schema(
        operation_summary="ارسال فرم تغذیه (Form2 - PWI)",
        request_body=PWISerializer,
        responses={201: PWISerializer}
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class Form3CreateView(CreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Form3.objects.all()
    serializer_class = Form3Serializer

    @swagger_auto_schema(
        operation_summary="ارسال فرم ۳",
        request_body=Form3Serializer,
        responses={201: Form3Serializer}
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class Form4CreateView(CreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Form4.objects.all()
    serializer_class = Form4Serializer

    @swagger_auto_schema(
        operation_summary="ارسال فرم ۴",
        request_body=Form4Serializer,
        responses={201: Form4Serializer}
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class MiddleFormCreateView(CreateAPIView):
    """
    ایجاد رکورد جدید MiddleForm
    """
    permission_classes = [permissions.AllowAny]
    queryset = MiddleForm.objects.all()
    serializer_class = MiddleFormSerializer

    @swagger_auto_schema(
        operation_summary="افزودن همسفره",
        operation_description=(
            "رکوردی شامل تعداد وعده مشترک، سطح ارتباط و سطح تاثیر ایجاد می‌کند.\n\n"
            "**Choices**\n"
            "- shared_meals_count: 1 | 2 | 3 | 4 | 5\n"
            "- relationship_level: family | friend | colleague | other\n"
            "- influence_level: none | low | medium | high | very_high\n"
        ),
        request_body=MiddleFormSerializer,
        responses={201: MiddleFormSerializer}
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)