# Generated by Django 5.1.1 on 2024-09-25 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Equipment", "0004_delete_client"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="equipment",
            name="unique_equipment_tag_plant",
        ),
        migrations.RenameField(
            model_name="equipment",
            old_name="equipmentTag",
            new_name="tag",
        ),
        migrations.RenameField(
            model_name="organization",
            old_name="organizationName",
            new_name="name",
        ),
        migrations.RenameField(
            model_name="plant",
            old_name="plantName",
            new_name="name",
        ),
        migrations.AddConstraint(
            model_name="equipment",
            constraint=models.UniqueConstraint(
                fields=("tag", "plant"), name="unique_equipment_tag_plant"
            ),
        ),
    ]
