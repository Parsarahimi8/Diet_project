from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings

# ----------form2-------1.3.0  -----diatery intake last week---------------------
class PastWeekIntake(models.Model):
    # ✅ کاربر
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="past_week_intakes",
        null=True, blank=True,
        verbose_name="کاربر"
    )

    class Eggs(models.TextChoices):
        zero = "0", "0"
        one = "1-2", "240"
        two = "3-4", "480"
        three = "4-6", "720"
        four = "+7", "1000"

    class Dairy(models.TextChoices):
        zero = "0", "0"
        one = "1-2", "500"
        two = "3-4", "1000"
        three = "4-6", "1500"
        four = "+7", "2000"

    class Meat(models.TextChoices):
        zero = "0", "0"
        one = "1-2", "130"
        two = "3-4", "260"
        three = "4-6", "390"
        four = "+7", "520"

    class Poultry(models.TextChoices):
        zero = "0", "0"
        one = "1-2", "160"
        two = "3-4", "320"
        three = "4-6", "480"
        four = "+7", "700"

    class Honey(models.TextChoices):
        zero = "0", "0"
        one = "1-2", "100"
        two = "3-4", "200"
        three = "4-6", "300"
        four = "+7", "400"

    class Fish(models.TextChoices):
        zero = "0", "0"
        one = "1-2", "200"
        two = "3-4", "400"
        three = "4-6", "600"
        four = "+7", "800"

    class Olive(models.TextChoices):
        zero = "0", "0"
        one = "1-2", "50"
        two = "3-4", "100"
        three = "4-6", "200"
        four = "+7", "400"

    class Sugar(models.TextChoices):
        zero = "0", "0"
        one = "1-2", "100"
        two = "3-4", "200"
        three = "4-6", "300"
        four = "+7", "400"

    class OilsM(models.TextChoices):
        zero = "0", "0"
        one = "1-2", "20"
        two = "3-4", "40"
        three = "4-6", "60"
        four = "+7", "100"

    class OilsS(models.TextChoices):
        zero = "0", "0"
        one = "1-2", "20"
        two = "3-4", "40"
        three = "4-6", "60"
        four = "+7", "100"

    class OilOlive(models.TextChoices):
        zero = "0", "0"
        one = "1-2", "20"
        two = "3-4", "40"
        three = "4-6", "60"
        four = "+7", "100"

    class Fruit(models.TextChoices):
        zero = "0", "0"
        one = "1-2", "300"
        two = "3-4", "600"
        three = "4-6", "900"
        four = "+7", "1200"

    class Vegetables(models.TextChoices):
        zero = "0", "0"
        one = "1-2", "150"
        two = "3-4", "300"
        three = "4-6", "450"
        four = "+7", "600"

    class Nuts(models.TextChoices):
        zero = "0", "0"
        one = "1-2", "60"
        two = "3-4", "120"
        three = "4-6", "180"
        four = "+7", "240"

    class Legumes(models.TextChoices):
        zero = "0", "0"
        one = "1-2", "300"
        two = "3-4", "600"
        three = "4-6", "900"
        four = "+7", "1200"

    class Potatoes(models.TextChoices):
        zero = "0", "0"
        one = "1-2", "400"
        two = "3-4", "800"
        three = "4-6", "1200"
        four = "+7", "1600"

    class Stimuli(models.TextChoices):
        zero = "0", "0"
        one = "1-2", "40"
        two = "3-4", "80"
        three = "4-6", "120"
        four = "+7", "160"

    class Rice(models.TextChoices):
        zero = "0", "0"
        one = "1-2", "400"
        two = "3-4", "800"
        three = "4-6", "1200"
        four = "+7", "1600"

    class Barley(models.TextChoices):
        zero = "0", "0"
        one = "1-2", "300"
        two = "3-4", "600"
        three = "4-6", "900"
        four = "+7", "1200"

    class Wheat(models.TextChoices):
        zero = "0", "0"
        one = "1-2", "400"
        two = "3-4", "800"
        three = "4-6", "1200"
        four = "+7", "1600"

    eggs = models.JSONField(default=dict)
    dairy = models.JSONField(default=dict)
    meat = models.JSONField(default=dict)
    poultry = models.JSONField(default=dict)
    honey = models.JSONField(default=dict)
    fish = models.JSONField(default=dict)
    olive = models.JSONField(default=dict)
    sugar = models.JSONField(default=dict)
    oilsM = models.JSONField(default=dict)
    oilsS = models.JSONField(default=dict)
    oilolive = models.JSONField(default=dict)
    fruit = models.JSONField(default=dict)
    vegetable = models.JSONField(default=dict)
    nuts = models.JSONField(default=dict)
    legumes = models.JSONField(default=dict)
    potatoes = models.JSONField(default=dict)
    stimuli = models.JSONField(default=dict)
    rice = models.JSONField(default=dict)
    barley = models.JSONField(default=dict)
    wheat = models.JSONField(default=dict)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "فرم رژیم غذایی فعلی"
        verbose_name_plural = "فرم‌های رژیم"
        ordering = ["-created_at"]

    def __str__(self):
        return f"PWI #{self.pk}"


# ---------- Form 3 ---preferred food ---1.4.0 ----------
class PreferrdFood(models.Model):
    # ✅ کاربر
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="preferred_foods",
        null=True, blank=True,
        verbose_name="کاربر"
    )

    Eggs = models.CharField(max_length=1)
    Dairy = models.CharField(max_length=1)
    Meat = models.CharField(max_length=1)
    Poultry = models.CharField(max_length=1)
    Honey = models.CharField(max_length=1)
    Fish = models.CharField(max_length=1)
    Olives = models.CharField(max_length=1)
    Sugar = models.CharField(max_length=1)
    OilsM = models.CharField(max_length=1)
    OilsS = models.CharField(max_length=1)
    Oil = models.CharField(max_length=1)
    Fruit = models.CharField(max_length=1)
    vegetables = models.CharField(max_length=1)
    Nuts = models.CharField(max_length=1)
    Legumes = models.CharField(max_length=1)
    Potatoes = models.CharField(max_length=1)
    Stimuli = models.CharField(max_length=1)
    Rice = models.CharField(max_length=1)
    Barley = models.CharField(max_length=1)
    Wheat = models.CharField(max_length=1)
    created_at = models.DateTimeField("ایجاد", auto_now_add=True)
    updated_at = models.DateTimeField("به‌روزرسانی", auto_now=True)


# ---------- Form 4 ----virtual shopping --- 1.5.0 ----------
class FreeShopping(models.Model):
    # ✅ کاربر
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="free_shoppings",
        null=True, blank=True,
        verbose_name="کاربر"
    )

    Eggs = models.CharField(max_length=1)
    Dairy = models.CharField(max_length=1)
    Meat = models.CharField(max_length=1)
    Poultry = models.CharField(max_length=1)
    Honey = models.CharField(max_length=1)
    Fish = models.CharField(max_length=1)
    Olives = models.CharField(max_length=1)
    Sugar = models.CharField(max_length=1)
    OilsM = models.CharField(max_length=1)
    OilsS = models.CharField(max_length=1)
    Oil = models.CharField(max_length=1)
    Fruit = models.CharField(max_length=1)
    vegetables = models.CharField(max_length=1)
    Nuts = models.CharField(max_length=1)
    Legumes = models.CharField(max_length=1)
    Potatoes = models.CharField(max_length=1)
    Stimuli = models.CharField(max_length=1)
    Rice = models.CharField(max_length=1)
    Barley = models.CharField(max_length=1)
    Wheat = models.CharField(max_length=1)
    created_at = models.DateTimeField("ایجاد", auto_now_add=True)
    updated_at = models.DateTimeField("به‌روزرسانی", auto_now=True)
