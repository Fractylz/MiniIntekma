# Generated by Django 5.1.1 on 2024-09-26 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Equipment", "0009_alter_equipment_driven_type_and_more"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="equipment",
            name="unique_equipment_tag_plant",
        ),
    ]
