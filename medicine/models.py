from django.db import models

# Create your models here.

class Medicine(models.Model):
    medicine_id=models.PositiveIntegerField(primary_key=True)
    medicine_name=models.CharField(max_length=100000)
    medicine_expirydate=models.DateField()
    medicine_mfgdate=models.DateField()


    def __str__(self):
        return self.supplier_name