from django.core.management.base import BaseCommand
from Equipment.models import Equipment


class Command(BaseCommand):
    help = "Sample"

    def handle(self, *args, **options):

        equipment_list = [
            "P123A",
            "P123B",
            "P123C",
        ]
        for e in equipment_list:
            Equipment.objects.create(tag = e)

        self.stdout.write(
            self.style.SUCCESS(
                "Added new equipments"
                )
            )
        
