from django.db import migrations

def load_food_groups(apps, schema_editor):
    FoodGroup = apps.get_model('Form', 'FoodGroup')

    food_groups_data = [
        {"id": 1, "code": 108, "title": "شیرینی", "categoryId": 1, "properties": {"description": "", "weeklyConsumptionOption": [100, 200, 300, 400], "score": {"price": 0.052437167, "health": 0.045447615, "environment": 0.361657678, "available": 0.2}, "imageName": "sweet", "unit": "کیلوگرم"}},
        {"id": 2, "code": 117, "title": "قهوه، چای، شکلات", "categoryId": 1, "properties": {"description": "(چای، قهوه و ...)", "weeklyConsumptionOption": [40, 80, 100, 160], "score": {"price": 0.650306881, "health": 1, "environment": 0.783126473, "available": 0.8}, "imageName": "caffeines-chocolates", "unit": "گرم"}},
        {"id": 3, "code": 105, "title": "عسل", "categoryId": 1, "properties": {"description": "(شیرین کننده طبیعی)", "weeklyConsumptionOption": [100, 200, 300, 400], "score": {"price": 0.62739279, "health": 0.027651312, "environment": 0.381221672, "available": 0.7}, "imageName": "honey", "unit": "کیلوگرم"}},
        {"id": 4, "code": 111, "title": "زیتون", "categoryId": 2, "properties": {"description": "", "weeklyConsumptionOption": [20, 40, 60, 100], "score": {"price": 0.576511198, "health": 0.705312792, "environment": 0.592745218, "available": 0.8}, "imageName": "olive-oil", "unit": "لیتر"}},
        {"id": 5, "code": 110, "title": "گیاهی", "categoryId": 2, "properties": {"description": "", "weeklyConsumptionOption": [20, 40, 60, 100], "score": {"price": 0.13272888, "health": 0.085911473, "environment": 0.517870527, "available": 0.3}, "imageName": "herbal-oil", "unit": "لیتر"}},
        {"id": 6, "code": 109, "title": "(کنجد، میوه‌ها، مغزها)", "categoryId": 2, "properties": {"description": "(بادام، کنجد و ...)", "weeklyConsumptionOption": [20, 40, 60, 100], "score": {"price": 0.580634479, "health": 0.179785814, "environment": 0.537256163, "available": 0.5}, "imageName": "sesame-nuts-oil", "unit": "لیتر"}},
        {"id": 7, "code": 116, "title": "سیب‌زمینی", "categoryId": 3, "properties": {"description": "", "weeklyConsumptionOption": [400, 800, 1200, 1600], "score": {"price": 0.046731611, "health": 0.198188596, "environment": 0.189108187, "available": 0.3}, "imageName": "potato", "unit": "کیلوگرم"}},
        {"id": 8, "code": 118, "title": "برنج", "categoryId": 3, "properties": {"description": "", "weeklyConsumptionOption": [400, 800, 1200, 1600], "score": {"price": 0.142344474, "health": 0.225041494, "environment": 0.471234331, "available": 0.2}, "imageName": "rice", "unit": "کیلوگرم"}},
        {"id": 9, "code": 120, "title": "نان", "categoryId": 3, "properties": {"description": "", "weeklyConsumptionOption": [400, 800, 1200, 1600], "score": {"price": 0.091579669, "health": 0.36279495, "environment": 0.346873699, "available": 0.1}, "imageName": "bread", "unit": "عدد"}},
        {"id": 10, "code": 106, "title": "ماهی", "categoryId": 4, "properties": {"description": "", "weeklyConsumptionOption": [200, 400, 600, 800], "score": {"price": 0.493521263, "health": 0.414581136, "environment": 0.120884442, "available": 0.9}, "imageName": "fish", "unit": "کیلوگرم"}},
        {"id": 11, "code": 103, "title": "گوشت قرمز", "categoryId": 4, "properties": {"description": "", "weeklyConsumptionOption": [130, 260, 390, 520], "score": {"price": 0.534866653, "health": 0.105825923, "environment": 0.961544236, "available": 0.5}, "imageName": "meat", "unit": "کیلوگرم"}},
        {"id": 12, "code": 104, "title": "گوشت مرغ", "categoryId": 4, "properties": {"description": "", "weeklyConsumptionOption": [160, 320, 480, 700], "score": {"price": 0.246737552, "health": 0.111565815, "environment": 0.621955327, "available": 0.5}, "imageName": "chicken", "unit": "کیلوگرم"}},
        {"id": 13, "code": 101, "title": "تخم‌مرغ", "categoryId": 4, "properties": {"description": "", "weeklyConsumptionOption": [240, 480, 720, 1000], "score": {"price": 0.166400617, "health": 0.219245964, "environment": 0.509421673, "available": 0.1}, "imageName": "egg", "unit": "عدد"}},
        {"id": 14, "code": 102, "title": "لبنیات", "categoryId": 4, "properties": {"description": "", "weeklyConsumptionOption": [500, 1000, 1500, 2000], "score": {"price": 0.235398854, "health": 0.091031041, "environment": 0.626881583, "available": 0.4}, "imageName": "dairy", "unit": "کیلوگرم"}},
        {"id": 15, "code": 113, "title": "سبزیجات", "categoryId": 5, "properties": {"description": "", "weeklyConsumptionOption": [150, 300, 450, 600], "score": {"price": 0.071732986, "health": 0.515841594, "environment": 0.196518445, "available": 0.3}, "imageName": "vegetable", "unit": "کیلوگرم"}},
        {"id": 16, "code": 107, "title": "خرما و زیتون", "categoryId": 5, "properties": {"description": "", "weeklyConsumptionOption": [50, 100, 200, 400], "score": {"price": 0.199317138, "health": 0.075853085, "environment": 0.353375346, "available": 0.9}, "imageName": "olive-dates", "unit": "کیلوگرم"}},
        {"id": 17, "code": 112, "title": "میوه‌ها", "categoryId": 5, "properties": {"description": "", "weeklyConsumptionOption": [300, 600, 900, 1200], "score": {"price": 0.105568121, "health": 0.167656772, "environment": 0.215678332, "available": 0.4}, "imageName": "fruits", "unit": "کیلوگرم"}},
        {"id": 18, "code": 114, "title": "آجیل‌ها", "categoryId": 6, "properties": {"description": "", "weeklyConsumptionOption": [60, 120, 180, 240], "score": {"price": 0.661319531, "health": 0.111961427, "environment": 0.502586663, "available": 0.7}, "imageName": "nuts", "unit": "کیلوگرم"}},
        {"id": 19, "code": 115, "title": "حبوبات", "categoryId": 6, "properties": {"description": "", "weeklyConsumptionOption": [300, 600, 900, 1200], "score": {"price": 0.164912835, "health": 0.192262777, "environment": 0.42163683, "available": 0.7}, "imageName": "beans", "unit": "کیلوگرم"}},
        {"id": 20, "code": 119, "title": "غلات", "categoryId": 6, "properties": {"description": "(جو، ذرت و ...)", "weeklyConsumptionOption": [300, 600, 900, 1200], "score": {"price": 0.057991613, "health": 0.214720181, "environment": 0.265593175, "available": 0.5}, "imageName": "cereals", "unit": "کیلوگرم"}},
    ]

    for item in food_groups_data:
        FoodGroup.objects.update_or_create(
            id=item["id"],
            defaults={
                "code": item["code"],
                "title": item["title"],
                "category_id": item["categoryId"],
                "properties": item["properties"],
            }
        )

class Migration(migrations.Migration):

    dependencies = [
        ('Form', '0026_remove_limitedshopping_offset_environment_and_more'),
    ]

    operations = [
        migrations.RunPython(load_food_groups),
    ]
