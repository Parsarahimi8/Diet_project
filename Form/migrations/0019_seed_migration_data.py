# -*- coding: utf-8 -*-
from django.db import migrations


def seed_reference_data(apps, schema_editor):
    Category = apps.get_model("Form", "Category")
    FoodGroup = apps.get_model("Form", "FoodGroup")

    categories = [
        (1, 'sugar-stimulants', 'قند و محرک\u200cها',
         {'bgColor': '#FAE8FF', 'iconColor': '#F1BEFF', 'titleColor': '#AD00DD', 'valuesColor': '#BF73D5'}),

        (2, 'oils', 'روغن\u200cها',
         {'bgColor': '#ECFCCB', 'iconColor': '#CDEE89', 'titleColor': '#537B01', 'valuesColor': '#9AE009'}),

        (3, 'carbohydrates', 'کربوهیدرات\u200cها',
         {'bgColor': '#FEF3C7', 'iconColor': '#FFE371', 'titleColor': '#A68500', 'valuesColor': '#FFD83D'}),

        (4, 'protein', 'پروتئین\u200c',
         {'bgColor': '#FEE2E2', 'iconColor': '#FFAAAA', 'titleColor': '#DC4F4F', 'valuesColor': '#FF3D3D'}),

        (5, 'fiber-vitamins', 'فیبر و ویتامین',
         {'bgColor': '#D1FAE5', 'iconColor': '#6AF5AE', 'titleColor': '#3D9769', 'valuesColor': '#0EA758'}),

        (6, 'combinations', 'ترکیبی\u200cها',
         {'bgColor': '#FEF3E2', 'iconColor': '#FFDDA8', 'titleColor': '#B17E2F', 'valuesColor': '#CC7D03'}),
    ]

    foodgroups = [
        (1, 108, 'sweet', 'شیرینی',
         {'description': '', 'imageName': 'sweet', 'weeklyConsumptionOption': [100, 200, 300, 400]}),

        (1, 117, 'caffeines-chocolates', 'قهوه، چای، شکلات',
         {'description': '(چای، قهوه و ...)', 'imageName': 'caffeines-chocolates', 'weeklyConsumptionOption': [40, 80, 100, 160]}),

        (1, 105, 'honey', 'عسل',
         {'description': '(شیرین کننده طبیعی)', 'imageName': 'honey', 'weeklyConsumptionOption': [100, 200, 300, 400]}),

        (2, 111, 'olive-oil', 'زیتون',
         {'description': '', 'imageName': 'olive-oil', 'weeklyConsumptionOption': [20, 40, 60, 100]}),

        (2, 110, 'herbal-oil', 'گیاهی',
         {'description': '', 'imageName': 'herbal-oil', 'weeklyConsumptionOption': [20, 40, 60, 100]}),

        (2, 109, 'sesame-nuts-oil', '(کنجد، میوه\u200cها، مغزها)',
         {'description': '(بادام، کنجد و ...)', 'imageName': 'sesame-nuts-oil', 'weeklyConsumptionOption': [20, 40, 60, 100]}),

        (3, 116, 'potato', 'سیب\u200cزمینی',
         {'description': '', 'imageName': 'potato', 'weeklyConsumptionOption': [400, 800, 1200, 1600]}),

        (3, 118, 'rice', 'برنج',
         {'description': '', 'imageName': 'rice', 'weeklyConsumptionOption': [400, 800, 1200, 1600]}),

        (3, 120, 'bread', 'نان',
         {'description': '', 'imageName': 'bread', 'weeklyConsumptionOption': [400, 800, 1200, 1600]}),

        (4, 106, 'fish', 'ماهی',
         {'description': '', 'imageName': 'fish', 'weeklyConsumptionOption': [200, 400, 600, 800]}),

        (4, 103, 'meat', 'گوشت قرمز',
         {'description': '', 'imageName': 'meat', 'weeklyConsumptionOption': [130, 260, 390, 520]}),

        (4, 104, 'chicken', 'گوشت مرغ',
         {'description': '', 'imageName': 'chicken', 'weeklyConsumptionOption': [160, 320, 480, 700]}),

        (4, 101, 'egg', 'تخم\u200cمرغ',
         {'description': '', 'imageName': 'egg', 'weeklyConsumptionOption': [240, 480, 720, 1000]}),

        (4, 102, 'dairy', 'لبنیات',
         {'description': '', 'imageName': 'dairy', 'weeklyConsumptionOption': [500, 1000, 1500, 2000]}),

        (5, 113, 'vegetable', 'سبزیجات',
         {'description': '', 'imageName': 'vegetable', 'weeklyConsumptionOption': [150, 300, 450, 600]}),

        (5, 107, 'olive-dates', 'خرما و زیتون',
         {'description': '', 'imageName': 'olive-dates', 'weeklyConsumptionOption': [50, 100, 200, 400]}),

        (5, 112, 'fruits', 'میوه\u200cها',
         {'description': '', 'imageName': 'fruits', 'weeklyConsumptionOption': [300, 600, 900, 1200]}),

        (6, 114, 'nuts', 'آجیل\u200cها',
         {'description': '', 'imageName': 'nuts', 'weeklyConsumptionOption': [60, 120, 180, 240]}),

        (6, 115, 'beans', 'حبوبات',
         {'description': '', 'imageName': 'beans', 'weeklyConsumptionOption': [300, 600, 900, 1200]}),

        (6, 119, 'cereals', 'غلات',
         {'description': '(جو، ذرت و ...)', 'imageName': 'cereals', 'weeklyConsumptionOption': [300, 600, 900, 1200]}),
    ]

    # 1) Upsert Categories by code
    cat_map = {}
    for code, name, title, props in categories:
        obj, _ = Category.objects.update_or_create(
            code=code,
            defaults={"name": name, "title": title, "properties": props},
        )
        cat_map[code] = obj

    # 2) Upsert FoodGroups by (category, code)
    for cat_code, fg_code, name, title, props in foodgroups:
        FoodGroup.objects.update_or_create(
            category=cat_map[cat_code],
            code=fg_code,
            defaults={"name": name, "title": title, "properties": props},
        )


class Migration(migrations.Migration):
    dependencies = [
        ("Form", "0018_alter_category_options_alter_foodgroup_options_and_more"),
    ]

    operations = [
        migrations.RunPython(seed_reference_data),
    ]
