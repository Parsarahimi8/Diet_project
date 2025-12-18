from django.urls import path
from .views import RegisterView, LoginView, ForgotPasswordView,VerifyOtpView,ResetPasswordView,LogoutView, CurrentUserView, TokenRefreshView

urlpatterns = [

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot-password'),
    path('verify-otp/', VerifyOtpView.as_view(), name='verify-otp'),
    path('reset-password/', ResetPasswordView.as_view(), name='reset-password'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('me/', CurrentUserView.as_view(), name='me'),
    path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),

]
