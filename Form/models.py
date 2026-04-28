from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from users.models import CustomUser


# ----------form2-------1.2.0  -----Tablemates Data---------------------

class Tablemate(models.Model):

    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="tablemates",
    )
    name = models.CharField(max_length=100)
    shared_meals_count = models.PositiveIntegerField(default=0)
    relationship_level = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )
    influence_level = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Tablemate"
        verbose_name_plural = "Tablemates"

    def __str__(self):
        return f"{self.name} (user={self.user.email})"

class Category(models.Model):
    code = models.IntegerField(unique=True, db_index=True)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)

    properties = models.JSONField(
        blank=True,
        null=True,
        default=dict,
    )

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ("code", "id")

    def __str__(self):
        return f"{self.title} (code={self.code})"


class FoodGroup(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="food_groups",
    )

    code = models.IntegerField(db_index=True)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)

    properties = models.JSONField(
        blank=True,
        null=True,
        default=dict,
    )

    class Meta:
        verbose_name = "Food Group"
        verbose_name_plural = "Food Groups"
        ordering = ("category__code", "code", "id")
        constraints = [
            models.UniqueConstraint(
                fields=["category", "code"],
                name="uniq_foodgroup_category_code"
            ),
        ]
    def __str__(self):
        return f"{self.title} (cat={self.category.code}, code={self.code})"


class PastWeekIntakes(models.Model):

    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="past_week_intakes",
    )
    food_group = models.ForeignKey(
        FoodGroup,
        on_delete=models.CASCADE,
        related_name="past_week_intakes",
        null=True
    )
    value = models.FloatField(
    )
    percent_usage = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = "Past Week Intake"
        verbose_name_plural = "Past Week Intakes"

    def __str__(self):
        return f"{self.user.email} - {self.food_group.title} on {self.date}"


class PreferredFood(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="preferred_foods",
    )
    food_group = models.ForeignKey(
        "FoodGroup",
        on_delete=models.CASCADE,
        related_name="preferred_by_users",
    )
    priority = models.PositiveSmallIntegerField(default=1)

    class Meta:
        verbose_name = "Preferred Food"
        verbose_name_plural = "Preferred Foods"
        ordering = ("user_id", "priority", "id")

    def __str__(self):
        return f"{self.user.email} - {self.food_group.title} (priority={self.priority})"


class FreeShopping(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="free_shoppings",
    )
    food_group = models.ForeignKey(
        "FoodGroup",
        on_delete=models.CASCADE,
        related_name="free_shopping_items",
    )
    value = models.FloatField()

    class Meta:
        ordering = ("user_id", "id")

    def __str__(self):
        return f"{self.user.email} - {self.food_group.title} (value={self.value})"


class LimitedShopping(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="limited_shoppings",
    )
    food_group = models.ForeignKey(
        "FoodGroup",
        on_delete=models.CASCADE,
        related_name="limited_shopping_items",
    )
    value = models.FloatField()
    offset_price = models.FloatField()
    offset_health = models.FloatField()
    offset_environment = models.FloatField()

    class Meta:
        ordering = ("user_id", "id")

    def __str__(self):
        return (
            f"{self.user.email} - {self.food_group.title} "
            f"(value={self.value}, price={self.offset_price}, "
            f"health={self.offset_health}, env={self.offset_environment})"
        )
