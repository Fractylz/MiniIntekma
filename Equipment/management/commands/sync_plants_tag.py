import pandas as pd
from django.core.management.base import BaseCommand
from Equipment.models import Equipment, Plant

class Command(BaseCommand):
    help = "This command imports Equipment tags and associated plants from an Excel file."

    def handle(self, *args, **kwargs):
        # Load the Excel file
        file_path = 'C:/Users/ariff/Downloads/VECTOR Database Simulator.xlsx'  # Update to your file path
        df = pd.read_excel(file_path, sheet_name='4. Equipment', usecols=['tag', 'plant'])
        
        # Prepare a list to hold Equipment objects
        equipment_objects = []

        for index, row in df.iterrows():
            tag = row['tag']
            plant_name = row['plant']

            # Skip rows with NaN in plant name
            if pd.isna(plant_name):
                self.stdout.write(self.style.WARNING(f"Skipping row with NaN plant name for tag: {tag}."))
                continue

            # Look up the related Plant object
            try:
                plant = Plant.objects.get(name=plant_name)
            except Plant.DoesNotExist:
                self.stdout.write(self.style.ERROR(f"Plant '{plant_name}' does not exist. Skipping this entry."))
                continue  # Skip this iteration if the plant does not exist

            # Create an Equipment object
            equipment_objects.append(Equipment(tag=tag, plant=plant))

        # Bulk insert into the database
        if equipment_objects:
            Equipment.objects.bulk_create(equipment_objects)
            self.stdout.write(self.style.SUCCESS(f"Successfully inserted {len(equipment_objects)} equipment records into the database."))
        else:
            self.stdout.write(self.style.WARNING("No equipment objects were inserted."))
