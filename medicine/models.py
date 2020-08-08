from django.db import models

# Create your models here.

class Medicine(models.Model):
    serial_no=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100000)
    manufacturing_date = models.DateField()
    expiry_date=models.DateField()


    def __str__(self):
        return self.name
'''
class Stock(models.Model):
    name=models.ForeignKey(Medicine,on_delete=models.CASCADE)
    stocks=models.PositiveIntegerField(primary_key=True,default=0)

    def __str__(self):
        return str(self.name)

'''