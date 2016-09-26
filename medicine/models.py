from django.db import models

# Create your models here.

class Medicine(models.Model):
    serial_no=models.PositiveIntegerField(primary_key=True)
    name=models.CharField(max_length=100000)
    manufacturing_date = models.DateField()
    expiry_date=models.DateField()
    stock_units=models.IntegerField(default=0)


    def __str__(self):
        return self.supplier_name