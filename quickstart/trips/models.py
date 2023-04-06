from django.db import models

# Create your models here.
class Trip(models.Model):
    
    class Meta:
        managed = False
        db_table = 'TRIPS'