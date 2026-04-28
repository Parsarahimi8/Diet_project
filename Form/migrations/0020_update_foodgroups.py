# -*- coding: utf-8 -*-
from django.db import migrations


def seed_foodgroups_update(apps, schema_editor):
    Category = apps.get_model("Form", "Category")
    FoodGroup = apps.get_model("Form", "FoodGroup")

    foodgroups = [
        (1, 108, "شیرینی", 1,
         {"description": "", "weeklyConsumptionOption": [100, 200, 300, 400],
          "score": {"price": 0.05, "health": 0.04, "environment": 0.36, "available": 0.2},
          "imageName": "sweet", "unit": "کیلوگرم"}),

        (2, 117, "قهوه، چای، شکلات", 1,
         {"description": "(چای، قهوه و ...)", "weeklyConsumptionOption": [40, 80, 100, 160],
          "score": {"price": 0.65, "health": 1, "environment": 0.78, "available": 0.8},
          "imageName": "caffeines-chocolates", "unit": "گرم"}),

        (3, 105, "عسل", 1,
         {"description": "(شیرین کننده طبیعی)", "weeklyConsumptionOption": [100, 200, 300, 400],
          "score": {"price": 0.62, "health": 0.02, "environment": 0.38, "available": 0.7},
          "imageName": "honey", "unit": "کیلوگرم"}),

        (4, 111, "زیتون", 2,
         {"description": "", "weeklyConsumptionOption": [20, 40, 60, 100],
          "score": {"price": 0.57, "health": 0.70, "environment": 0.59, "available": 0.8},
          "imageName": "olive-oil", "unit": "لیتر"}),

        (5, 110, "گیاهی", 2,
         {"description": "", "weeklyConsumptionOption": [20, 40, 60, 100],
          "score": {"price": 0.13, "health": 0.08, "environment": 0.51, "available": 0.3},
          "imageName": "herbal-oil", "unit": "لیتر"}),

        (6, 109, "(کنجد، میوه‌ها، مغزها)", 2,
         {"description": "(بادام، کنجد و ...)", "weeklyConsumptionOption": [20, 40, 60, 100],
          "score": {"price": 0.58, "health": 0.17, "environment": 0.53, "available": 0.5},
          "imageName": "sesame-nuts-oil", "unit": "لیتر"}),

        (7, 116, "سیب‌زمینی", 3,
         {"description": "", "weeklyConsumptionOption": [400, 800, 1200, 1600],
          "score": {"price": 0.04, "health": 0.19, "environment": 0.18, "available": 0.3},
          "imageName": "potato", "unit": "کیلوگرم"}),

        (8, 118, "برنج", 3,
         {"description": "", "weeklyConsumptionOption": [400, 800, 1200, 1600],
          "score": {"price": 0.14, "health": 0.22, "environment": 0.47, "available": 0.2},
          "imageName": "rice", "unit": "کیلوگرم"}),

        (9, 120, "نان", 3,
         {"description": "", "weeklyConsumptionOption": [400, 800, 1200, 1600],
          "score": {"price": 0.09, "health": 0.36, "environment": 0.34, "available": 0.1},
          "imageName": "bread", "unit": "عدد"}),

        (10, 106, "ماهی", 4,
         {"description": "", "weeklyConsumptionOption": [200, 400, 600, 800],
          "score": {"price": 0.49, "health": 0.41, "environment": 0.12, "available": 0.9},
          "imageName": "fish", "unit": "کیلوگرم"}),

        (11, 103, "گوشت قرمز", 4,
         {"description": "", "weeklyConsumptionOption": [130, 260, 390, 520],
          "score": {"price": 0.53, "health": 0.10, "environment": 0.96, "available": 0.5},
          "imageName": "meat", "unit": "کیلوگرم"}),

        (12, 104, "گوشت مرغ", 4,
         {"description": "", "weeklyConsumptionOption": [160, 320, 480, 700],
          "score": {"price": 0.24, "health": 0.11, "environment": 0.62, "available": 0.5},
          "imageName": "chicken", "unit": "کیلوگرم"}),

        (13, 101, "تخم‌مرغ", 4,
         {"description": "", "weeklyConsumptionOption": [240, 480, 720, 1000],
          "score": {"price": 0.16, "health": 0.21, "environment": 0.50, "available": 0.1},
          "imageName": "egg", "unit": "عدد"}),

        (14, 102, "لبنیات", 4,
         {"description": "", "weeklyConsumptionOption": [500, 1000, 1500, 2000],
          "score": {"price": 0.23, "health": 0.09, "environment": 0.62, "available": 0.4},
          "imageName": "dairy", "unit": "کیلوگرم"}),

        (15, 113, "سبزیجات", 5,
         {"description": "", "weeklyConsumptionOption": [150, 300, 450, 600],
          "score": {"price": 0.07, "health": 0.51, "environment": 0.19, "available": 0.3},
          "imageName": "vegetable", "unit": "کیلوگرم"}),

        (16, 107, "خرما و زیتون", 5,
         {"description": "", "weeklyConsumptionOption": [50, 100, 200, 400],
          "score": {"price": 0.19, "health": 0.07, "environment": 0.35, "available": 0.9},
          "imageName": "olive-dates", "unit": "کیلوگرم"}),

        (17, 112, "میوه‌ها", 5,
         {"description": "", "weeklyConsumptionOption": [300, 600, 900, 1200],
          "score": {"price": 0.10, "health": 0.16, "environment": 0.21, "available": 0.4},
          "imageName": "fruits", "unit": "کیلوگرم"}),

        (18, 114, "آجیل‌ها", 6,
         {"description": "", "weeklyConsumptionOption": [60, 120, 180, 240],
          "score": {"price": 0.66, "health": 0.11, "environment": 0.50, "available": 0.7},
          "imageName": "nuts", "unit": "کیلوگرم"}),

        (19, 115, "حبوبات", 6,
         {"description": "", "weeklyConsumptionOption": [300, 600, 900, 1200],
          "score": {"price": 0.16, "health": 0.19, "environment": 0.42, "available": 0.7},
          "imageName": "beans", "unit": "کیلوگرم"}),

        (20, 119, "غلات", 6,
         {"description": "(جو، ذرت و ...)", "weeklyConsumptionOption": [300, 600, 900, 1200],
          "score": {"price": 0.05, "health": 0.21, "environment": 0.26, "available": 0.5},
          "imageName": "cereals", "unit": "کیلوگرم"}),
    ]

    # Upsert
    for id_, code, title, category_id, props in foodgroups:
        category = Category.objects.get(code=category_id)
        FoodGroup.objects.update_or_create(
            code=code,
            category=category,
            defaults={
                "title": title,
                "category": category,
                "properties": props,
            },
        )


class Migration(migrations.Migration):
    dependencies = [
        ("Form", "0019_seed_migration_data"),
    ]

    operations = [
        migrations.RunPython(seed_foodgroups_update),
    ]
