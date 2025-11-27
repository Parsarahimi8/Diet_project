from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# ------form 1 ------: 1.1.0------------------
class DemographicFormInformation(models.Model):
    # ---- Enums ----
    class Gender(models.TextChoices):
        MALE = "male", "مرد"
        FEMALE = "female", "زن"
        OTHER = "other", "سایر"

    class JobState(models.TextChoices):
        EMPLOYED = "employed", "شاغل"
        STUDENT = "student", "محصل"
        OTHER = "other", "سایر"

    class IncomeBracket(models.TextChoices):
        R0_10 = "0-10", "0-10"
        R10_30 = "10-30", "10-30"
        R30_50 = "30-50", "30-50"
        R50_70 = "50-70", "50-70"
        R70_90 = "70-90", "70-90"
        R90_PLUS = "90+", "more than 90"

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
        ARDABIL = "ardabil", "اردبیل"
        ESFAHAN = "esfahan", "اصفهان"
        ALBORZ = "alborz", "البرز"
        ILAM = "ilam", "ایلام"
        BUSHEHR = "bushehr", "بوشهر"
        TEHRAN = "tehran", "تهران"
        CH_BAKHT = "chaharmahal_bakhtiari", "چهارمحال و بختیاری"
        KH_JONOOBI = "khorasan_jonoobi", "خراسان جنوبی"
        KH_RAZAVI = "khorasan_razavi", "خراسان رضوی"
        KH_SHOMALI = "khorasan_shomali", "خراسان شمالی"
        KHUZESTAN = "khuzestan", "خوزستان"
        ZANJAN = "zanjan", "زنجان"
        SEMNAN = "semnan", "سمنان"
        SISTAN = "sistan_baluchestan", "سیستان و بلوچستان"
        FARS = "fars", "فارس"
        QAZVIN = "qazvin", "قزوین"
        QOM = "qom", "قم"
        KURDISTAN = "kurdistan", "کردستان"
        KERMAN = "kerman", "کرمان"
        KERMANSHAH = "kermanshah", "کرمانشاه"
        KOHGILUYEH = "kohgiluyeh_boyerahmad", "کهگیلویه و بویراحمد"
        GOLESTAN = "golestan", "گلستان"
        GILAN = "gilan", "گیلان"
        LORESTAN = "lorestan", "لرستان"
        MAZANDARAN = "mazandaran", "مازندران"
        MARKAZI = "markazi", "مرکزی"
        HORMOZG = "hormozgan", "هرمزگان"
        HAMEDAN = "hamedan", "همدان"
        YAZD = "yazd", "یزد"

    # ---- Required fields (cannot be null/blank) ----
    name = models.CharField("نام", max_length=120)  # required
    age = models.PositiveSmallIntegerField(
        "سن",
        validators=[MinValueValidator(1), MaxValueValidator(120)]
    )  # required
    gender = models.CharField(
        "جنسیت",
        max_length=10,
        choices=Gender.choices
    )  # required

    # ---- Optional fields (nullable) ----
    height_cm = models.PositiveSmallIntegerField(
        "قد (سانتی‌متر)",
        validators=[MinValueValidator(50), MaxValueValidator(250)],
        null=True, blank=True
    )
    weight_kg = models.FloatField(
        "وزن (کیلوگرم)",
        validators=[MinValueValidator(20), MaxValueValidator(400)],
        null=True, blank=True
    )
    education = models.CharField(
        "تحصیلات",
        max_length=100,
        null=True, blank=True
    )
    job_state = models.CharField(
        "وضعیت شغلی/تحصیلی",
        max_length=10,
        choices=JobState.choices,
        null=True, blank=True
    )
    income_bracket = models.CharField(
        "وضعیت درآمد (میلیون)",
        max_length=10,
        choices=IncomeBracket.choices,
        null=True, blank=True
    )
    diet_income_percent = models.PositiveSmallIntegerField(
        "درصد درآمدِ تخصیص‌یافته به رژیم",
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        null=True, blank=True
    )
    province = models.CharField(
        "استان",
        max_length=32,
        choices=Province.choices,
        null=True, blank=True
    )
    marital_status = models.CharField(
        "وضعیت تاهل",
        max_length=10,
        choices=MaritalStatus.choices,
        null=True, blank=True
    )
    family_members = models.PositiveSmallIntegerField(
        "تعداد اعضای خانواده",
        validators=[MinValueValidator(1), MaxValueValidator(30)],
        null=True, blank=True
    )
    sport_days_per_week = models.CharField(
        "تعداد روزهای ورزش در هفته",
        max_length=5,
        choices=SportDaysPerWeek.choices,
        null=True, blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "فرم دموگرافیک"
        verbose_name_plural = "فرم‌های دموگرافیک"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.get_province_display() if self.province else '—'}"



# ------Household$social-------- 1.2.0-----middleform------------


class Tablemates(models.Model):


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
    name = models.CharField(max_length=100, null=True)
    shared_meals_count = models.PositiveSmallIntegerField(
        "تعداد وعده مشترک",
        choices=SharedMeals.choices,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        null=True, blank=True

    )
    relationship_level = models.CharField(
        "سطح ارتباط",
        max_length=16,
        choices=RelationshipLevel.choices,
        null=True, blank=True

    )
    influence_level = models.CharField(
        "سطح تاثیر",
        max_length=16,
        choices=InfluenceLevel.choices,
        null=True, blank=True

    )
    created_at = models.DateTimeField("ایجاد", auto_now_add=True)
    updated_at = models.DateTimeField("به‌روزرسانی", auto_now=True)

    class Meta:
        verbose_name = "افزودن همسفره"
        verbose_name_plural = "افزودن همسفره"
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["relationship_level"]),
            models.Index(fields=["influence_level"]),
            models.Index(fields=["created_at"]),
        ]

    def __str__(self):
        return f"MiddleForm #{self.pk} - {self.get_relationship_level_display()} / {self.get_influence_level_display()}"


# ----------form2-------1.3.0  -----diatery intake last week---------------------
class PastWeekIntake(models.Model):

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

    eggs = models.CharField(
        max_length=10,
        choices=Eggs.choices
    )
    dairy = models.CharField(
        max_length=10,
        choices=Dairy.choices
    )
    meat = models.CharField(
        max_length=10,
        choices=Meat.choices
    )
    poultry = models.CharField(
        max_length=10,
        choices=Eggs.choices
    )
    honey = models.CharField(
        max_length=10,
        choices=Honey.choices
    )
    fish = models.CharField(
        max_length=10,
        choices=Fish.choices
    )
    olive = models.CharField(
        max_length=10,
        choices=Olive.choices
    )
    sugar = models.CharField(
        max_length=10,
        choices=Sugar.choices
    )

    oilsM = models.CharField(
        max_length=10,
        choices=OilsM.choices
    )
    oilsS = models.CharField(
        max_length=10,
        choices=OilsS.choices
    )

    oilolive = models.CharField(
        max_length=10,
        choices=OilOlive.choices
    )
    fruit = models.CharField(
        max_length=10,
        choices=Fruit.choices
    )

    vegetable = models.CharField(
        max_length=10,
        choices=Vegetables.choices
    )

    nuts = models.CharField(
        max_length=10,
        choices=Nuts.choices
    )

    legumes = models.CharField(
        max_length=10,
        choices=Legumes.choices
    )

    potatoes = models.CharField(
        max_length=10,
        choices=Potatoes.choices
    )

    stimuli = models.CharField(
        max_length=10,
        choices=Stimuli.choices
    )
    rice = models.CharField(
        max_length=10,
        choices=Rice.choices
    )

    barley = models.CharField(
        max_length=10,
        choices=Barley.choices
    )
    wheat = models.CharField(
        max_length=10,
        choices=Wheat.choices
    )
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

