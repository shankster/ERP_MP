from django.db import models

# Create your models here.

class Supplier(models.Model):
    supplier_id=models.PositiveIntegerField(primary_key=True)
    supplier_name=models.CharField(max_length=100000)
    city=models.CharField(max_length=100000)
    email_id=models.CharField(max_length=10000)

    def __str__(self):
        return self.supplier_name