from django.db import models
from django.utils.timezone import now

# Create your models here.
class Location(models.Model):
    unique_id=models.AutoField(primary_key=True, null=False)
    location=models.CharField(max_length=255, null=False)
    date_added = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return self.location

class Departments(models.Model):
    unique_id=models.AutoField(primary_key=True, null=False)
    department_name=models.CharField(max_length=255, null=False)
    location=models.ForeignKey(Location, on_delete=models.CASCADE)
    date_added = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return self.department_name
