from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class DemographicForm(models.Model):
    # ---- Enums (همه داخل همین کلاس) ----
    class Gender(models.TextChoices):
        MALE = "male", "مرد"
        FEMALE = "female", "زن"

    class JobState(models.TextChoices):
        EMPLOYED = "employed", "شاغل"
        STUDENT = "student", "محصل"
        OTHER = "other", "سایر"

    class IncomeBracket(models.TextChoices):
        R0_10    = "0-10",   "0-10"
        R10_30   = "10-30",  "10-30"
        R30_50   = "30-50",  "30-50"
        R50_70   = "50-70",  "50-70"
        R70_90   = "70-90",  "70-90"
        R90_PLUS = "90+",    "more than 90"

    class SportDaysPerWeek(models.TextChoices):
        D0_2 = "0-2", "0-2"
        D1_3 = "1-3", "1-3"
        D2_4 = "2-4", "2-4"
        D3_5 = "3-5", "3-5"
        D4_6 = "4-6", "4-6"

    class MaritalStatus(models.TextChoices):
        SINGLE = "single", "مجرد"
        MARRIED = "married", "متاهل"

    class Province(models.TextChoices):
        AZ_SHARQI = "azarbaijan_sharqi", "آذربایجان شرقی"
        AZ_GHARBI = "azarbaijan_gharbi", "آذربایجان غربی"
        ARDABIL   = "ardabil", "اردبیل"
        ESFAHAN   = "esfahan", "اصفهان"
        ALBORZ    = "alborz", "البرز"
        ILAM      = "ilam", "ایلام"
        BUSHEHR   = "bushehr", "بوشهر"
        TEHRAN    = "tehran", "تهران"
        CH_BAKHT  = "chaharmahal_bakhtiari", "چهارمحال و بختیاری"
        KH_JONOOBI= "khorasan_jonoobi", "خراسان جنوبی"
        KH_RAZAVI = "khorasan_razavi", "خراسان رضوی"
        KH_SHOMALI= "khorasan_shomali", "خراسان شمالی"
        KHUZESTAN = "khuzestan", "خوزستان"
        ZANJAN    = "zanjan", "زنجان"
        SEMNAN    = "semnan", "سمنان"
        SISTAN    = "sistan_baluchestan", "سیستان و بلوچستان"
        FARS      = "fars", "فارس"
        QAZVIN    = "qazvin", "قزوین"
        QOM       = "qom", "قم"
        KURDISTAN = "kurdistan", "کردستان"
        KERMAN    = "kerman", "کرمان"
        KERMANSHAH= "kermanshah", "کرمانشاه"
        KOHGILUYEH= "kohgiluyeh_boyerahmad", "کهگیلویه و بویراحمد"
        GOLESTAN  = "golestan", "گلستان"
        GILAN     = "gilan", "گیلان"
        LORESTAN  = "lorestan", "لرستان"
        MAZANDARAN= "mazandaran", "مازندران"
        MARKAZI   = "markazi", "مرکزی"
        HORMOZG   = "hormozgan", "هرمزگان"
        HAMEDAN   = "hamedan", "همدان"
        YAZD      = "yazd", "یزد"

    # ---- Fields ----
    name = models.CharField("نام", max_length=120)
    age = models.PositiveSmallIntegerField("سن", validators=[MinValueValidator(1), MaxValueValidator(120)])
    gender = models.CharField("جنسیت", max_length=10, choices=Gender.choices)

    height_cm = models.PositiveSmallIntegerField("قد (سانتی‌متر)", validators=[MinValueValidator(50), MaxValueValidator(250)])
    weight_kg = models.FloatField("وزن (کیلوگرم)", validators=[MinValueValidator(20), MaxValueValidator(400)])

    education = models.CharField("تحصیلات", max_length=100)

    job_state = models.CharField("وضعیت شغلی/تحصیلی", max_length=10, choices=JobState.choices)

    income_bracket = models.CharField("وضعیت درآمد (میلیون)", max_length=10, choices=IncomeBracket.choices)

    diet_income_percent = models.PositiveSmallIntegerField(
        "درصد درآمدِ تخصیص‌یافته به رژیم",
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )

    province = models.CharField("استان", max_length=32, choices=Province.choices)  # 32 کفایت می‌کند

    marital_status = models.CharField("وضعیت تاهل", max_length=10, choices=MaritalStatus.choices)

    family_members = models.PositiveSmallIntegerField("تعداد اعضای خانواده", validators=[MinValueValidator(1), MaxValueValidator(30)])

    sport_days_per_week = models.CharField(
        "تعداد روزهای ورزش در هفته",
        max_length=5,
        choices=SportDaysPerWeek.choices
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "فرم دموگرافیک"
        verbose_name_plural = "فرم‌های دموگرافیک"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.get_province_display()}"


class Form2(models.Model):
    title = models.CharField("عنوان", max_length=120, blank=True, default="")
    data = models.JSONField("داده‌های فرم", blank=True, default=dict)  # هر ساختاری که بخوای
    created_at = models.DateTimeField("ایجاد", auto_now_add=True)
    updated_at = models.DateTimeField("به‌روزرسانی", auto_now=True)

    class Meta:
        verbose_name = "فرم ۲"
        verbose_name_plural = "فرم‌های ۲"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title or f"Form2 #{self.pk}"


# ---------- Form 3 ----------
class Form3(models.Model):
    title = models.CharField("عنوان", max_length=120, blank=True, default="")
    data = models.JSONField("داده‌های فرم", blank=True, default=dict)
    is_active = models.BooleanField("فعال؟", default=True)
    created_at = models.DateTimeField("ایجاد", auto_now_add=True)
    updated_at = models.DateTimeField("به‌روزرسانی", auto_now=True)

    class Meta:
        verbose_name = "فرم ۳"
        verbose_name_plural = "فرم‌های ۳"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title or f"Form3 #{self.pk}"


# ---------- Form 4 ----------
class Form4(models.Model):
    title = models.CharField("عنوان", max_length=120, blank=True, default="")
    notes = models.TextField("یادداشت‌ها", blank=True, default="")
    data = models.JSONField("داده‌های فرم", blank=True, default=dict)
    created_at = models.DateTimeField("ایجاد", auto_now_add=True)
    updated_at = models.DateTimeField("به‌روزرسانی", auto_now=True)

    class Meta:
        verbose_name = "فرم ۴"
        verbose_name_plural = "فرم‌های ۴"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title or f"Form4 #{self.pk}"


class MiddleForm(models.Model):
    class SharedMeals(models.IntegerChoices):
        ONE   = 1, "۱"
        TWO   = 2, "۲"
        THREE = 3, "۳"
        FOUR  = 4, "۴"
        FIVE  = 5, "۵"

    class RelationshipLevel(models.TextChoices):
        FAMILY   = "family", "خانواده"
        FRIEND   = "friend", "دوست"
        COLLEAGUE= "colleague", "همکار"
        OTHER    = "other", "سایر"

    class InfluenceLevel(models.TextChoices):
        NONE      = "none", "هیچ"
        LOW       = "low", "کم"
        MEDIUM    = "medium", "متوسط"
        HIGH      = "high", "زیاد"
        VERY_HIGH = "very_high", "خیلی زیاد"

    # ---- Fields ----
    shared_meals_count = models.PositiveSmallIntegerField(
        "تعداد وعده مشترک",
        choices=SharedMeals.choices,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
    )
    relationship_level = models.CharField(
        "سطح ارتباط",
        max_length=16,
        choices=RelationshipLevel.choices,
    )
    influence_level = models.CharField(
        "سطح تاثیر",
        max_length=16,
        choices=InfluenceLevel.choices,
    )
    created_at = models.DateTimeField("ایجاد", auto_now_add=True)
    updated_at = models.DateTimeField("به‌روزرسانی", auto_now=True)

    class Meta:
        verbose_name = "فرم میانی"
        verbose_name_plural = "فرم‌های میانی"
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["relationship_level"]),
            models.Index(fields=["influence_level"]),
            models.Index(fields=["created_at"]),
        ]

    def __str__(self):
        return f"MiddleForm #{self.pk} - {self.get_relationship_level_display()} / {self.get_influence_level_display()}"
