from django.db import migrations

def shift_foodgroup_ids_sqlite(apps, schema_editor):
    cursor = schema_editor.connection.cursor()

    # 1) حذف رکورد id = 1
    cursor.execute("DELETE FROM Form_foodgroup WHERE id = 1;")

    # 2) تبدیل id = 2 → 1
    cursor.execute("""
        UPDATE Form_foodgroup
        SET id = 1
        WHERE id = 2;
    """)

    # 3) آپدیت FK ها (جدول‌های واقعی)
    fk_tables = [
        ('Form_pastweekintakes', 'food_group_id'),
        ('Form_preferredfood', 'food_group_id'),
    ]

    # FK = 2 → 1
    for table, col in fk_tables:
        cursor.execute(f"""
            UPDATE {table}
            SET {col} = 1
            WHERE {col} = 2;
        """)

    # 4) id های بزرگ‌تر از 2 یک واحد کاهش یابند
    cursor.execute("""
        UPDATE Form_foodgroup
        SET id = id - 1
        WHERE id > 2;
    """)

    # 5) FK های بزرگ‌تر از 2 یک واحد کاهش یابند
    for table, col in fk_tables:
        cursor.execute(f"""
            UPDATE {table}
            SET {col} = {col} - 1
            WHERE {col} > 2;
        """)


def reverse_shift_foodgroup_ids_sqlite(apps, schema_editor):
    pass  # برعکس‌سازی لازم نیست


class Migration(migrations.Migration):

    dependencies = [
        ("Form", "0020_update_foodgroups"),
    ]

    operations = [
        migrations.RunPython(
            shift_foodgroup_ids_sqlite,
            reverse_shift_foodgroup_ids_sqlite,
        )
    ]
