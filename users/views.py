from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from .serializers import RegisterSerializer, LoginSerializer, VerifyOtpSerializer, ResetPasswordSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.mail import send_mail
from django.conf import settings
import random
from .models import CustomUser
from drf_yasg import openapi


class RegisterView(APIView):
    parser_classes = [JSONParser]

    @swagger_auto_schema(request_body=RegisterSerializer)
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class LoginView(APIView):
    parser_classes = [JSONParser]

    @swagger_auto_schema(request_body=LoginSerializer)
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)
        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        })


class ForgotPasswordView(APIView):
    parser_classes = [JSONParser]

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'email': openapi.Schema(type=openapi.TYPE_STRING, description='Email of user'),
            },
            required=['email']
        )
    )
    def post(self, request):
        email = request.data.get('email')
        if not email:
            return Response({"error": "Email is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        # Generate and store OTP with timestamp (as string)
        otp = f"{random.randint(100000, 999999)}"
        user.set_otp(otp)

        send_mail(
            subject='Your OTP Code',
            message=f'Your OTP code is {otp}',
            from_email=getattr(settings, "DEFAULT_FROM_EMAIL", "no-reply@example.com"),
            recipient_list=[email],
            fail_silently=False,
        )
        return Response({"message": "OTP sent to your email"}, status=status.HTTP_200_OK)


class VerifyOtpView(APIView):

    @swagger_auto_schema(request_body=VerifyOtpSerializer)
    def post(self, request):
        serializer = VerifyOtpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        otp = serializer.validated_data['otp']

        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        # Use model method and clear OTP after success
        if user.verify_otp(otp):
            return Response({"message": "OTP verified successfully"}, status=status.HTTP_200_OK)

        return Response({"error": "Invalid or expired OTP"}, status=status.HTTP_400_BAD_REQUEST)


class ResetPasswordView(APIView):

    @swagger_auto_schema(request_body=ResetPasswordSerializer)
    def post(self, request):
        serializer = ResetPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        otp = serializer.validated_data['otp']
        new_password = serializer.validated_data['new_password']

        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        # Verify OTP from model, then reset password and clear OTP
        if not user.verify_otp(otp):
            return Response({"error": "Invalid or expired OTP"}, status=status.HTTP_400_BAD_REQUEST)

        user.set_password(new_password)
        user.clear_otp()
        user.save()

        return Response({"message": "Password reset successfully"}, status=status.HTTP_200_OK)
