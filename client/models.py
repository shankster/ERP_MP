from django.db import models
#from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator

# Create your models here.

class Client(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    email_id=models.EmailField(help_text="Enter Valid Email ID")
    contact_number=models.CharField(max_length=10,help_text="Enter STD Code for landline numbers",default="")


    def __str__(self):
        return self.name