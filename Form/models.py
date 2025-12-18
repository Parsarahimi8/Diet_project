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

    def __str__(self):
        return self.title or self.name

class FoodGroup(models.Model):

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="food_groups",
    )
    code = models.IntegerField()
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

    def __str__(self):
        return f"{self.title} (code={self.code})"

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
    percent_usage = models.FloatField(blank=True)
    date = models.DateTimeField(auto_now=True,null=True)

    class Meta:
        verbose_name = "Past Week Intake"
        verbose_name_plural = "Past Week Intakes"

    def __str__(self):
        return f"{self.user.email} - {self.food_group.title} on {self.date}"
