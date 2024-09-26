import pandas as pd
from django.core.management.base import BaseCommand
from Equipment.models import Equipment  

class Command(BaseCommand):
    help = "Python script to import all the equipment tags into equipment model from table 4. Equipment column = tag"

    def handle(self, *args, **kwargs):
        # Step 1: Load the Excel file and extract the 'tag' column
        file_path = "C:/Users/ariff/Downloads/VECTOR Database Simulator.xlsx"  
        df = pd.read_excel(file_path, sheet_name='4. Equipment', usecols=['tag'])
        
        # Step 2: Extract the 'tag' column as a list, dropping any NaN values
        tag_list = df['tag'].dropna().tolist()

        # Step 3: Create Equipment objects for bulk creation
        equipment_objects = [Equipment(tag=tag) for tag in tag_list]

        # Step 4: Bulk insert into the database
        Equipment.objects.bulk_create(equipment_objects)

        # Output how many records were inserted
        self.stdout.write(self.style.SUCCESS(f"Successfully inserted {len(equipment_objects)} equipment tags into the database."))


