from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.utils import timezone
import datetime


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        if not password:
            raise ValueError("Password is required")
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        if not password:
            raise ValueError("Superuser must have a password.")
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=30, blank=False)
    age = models.PositiveIntegerField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    properties = models.JSONField(blank=True, null=True, default=dict)
    otp = models.CharField(max_length=6, blank=True, null=True)
    otp_created_at = models.DateTimeField(blank=True, null=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_users',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_users',
        blank=True
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    # ----- OTP helpers -----
    def set_otp(self, otp_code):
        """Set OTP (always as string) and record timestamp."""
        self.otp = str(otp_code)
        self.otp_created_at = timezone.now()
        self.save(update_fields=['otp', 'otp_created_at'])

    def verify_otp(self, otp_code, expiry_minutes=10):
        """Check if OTP matches and is still valid."""
        if not self.otp or not self.otp_created_at:
            return False
        if str(self.otp) != str(otp_code):
            return False
        now = timezone.now()
        if now - self.otp_created_at > datetime.timedelta(minutes=expiry_minutes):
            return False
        return True

    # alias for backward compatibility
    def is_otp_valid(self, otp_code, expiry_minutes=10):
        return self.verify_otp(otp_code, expiry_minutes)

    def clear_otp(self):
        """Remove OTP and timestamp after verification."""
        self.otp = None
        self.otp_created_at = None
        self.save(update_fields=['otp', 'otp_created_at'])
