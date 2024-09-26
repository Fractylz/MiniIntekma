import pandas as pd
from django.core.management.base import BaseCommand
from Equipment.models import Plant

class Command(BaseCommand):
    help = "Python script to import all the plant into plant model from table 4. Equipment column = plant"

    def handle(self, *args, **kwargs):
        # Step 1: Load the Excel file and extract the 'tag' column
        file_path = "C:/Users/ariff/Downloads/VECTOR Database Simulator.xlsx"  
        df = pd.read_excel(file_path, sheet_name='4. Equipment', usecols=['plant'])
        
        # Step 2: Extract the 'tag' column as a list, dropping any NaN values
        plant_list = df['plant'].dropna().tolist()

        # Step 3: Create Equipment objects for bulk creation
        plant_objects = [Plant(name=plant) for plant in plant_list]

        # Step 4: Bulk insert into the database
        Plant.objects.bulk_create(plant_objects)

        # Output how many records were inserted
        self.stdout.write(self.style.SUCCESS(f"Successfully inserted {len(plant_objects)} plants into the database."))
