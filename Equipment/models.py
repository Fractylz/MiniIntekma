from django.db import models


class DriverType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class DrivenType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Organization(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Plant(models.Model):
    name = models.CharField(max_length=255)
    client = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True, related_name='plants')

    def __str__(self):
        return self.name  

class Equipment(models.Model):
    tag = models.CharField(max_length=255)
    plant = models.ForeignKey('Plant', on_delete=models.CASCADE, null=True)
    driver_type = models.ForeignKey(DriverType, on_delete=models.CASCADE, blank=True, null=True)
    driven_type = models.ForeignKey(DrivenType, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:#constraint to prevent duplicate values
        constraints = [
            models.UniqueConstraint(fields=['tag', 'plant'], name='unique_equipment_tag_plant')
        ]

    def __str__(self):
        return f"{self.tag}"
 
