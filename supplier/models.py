from django.db import models

# Create your models here.

class Supplier(models.Model):
    VARANASI='VSB'
    NEW_DELHI='DEL'
    MUMBAI='BOM'
    CHENNAI='MAA'
    VISHAKAPATHANAM='VSKP'
    DURGAPUR='RDP'
    KOLKATA='CCU'
    SHIMLA='SHM'
    CITY_LIST=(
        (VARANASI,'Varanasi'),
        (NEW_DELHI,'New Delhi'),
        (MUMBAI,'Mumbai'),
        (CHENNAI, 'Chennai'),
        (VISHAKAPATHANAM, 'Vishakapatanam'),
        (DURGAPUR, 'Durgapur'),
        (KOLKATA, 'Kolkata'),
        (SHIMLA, 'Shimla'),
        )
    supplier_ID=models.AutoField(primary_key=True)
    supplier_name=models.CharField(max_length=1000000)
    city=models.CharField(max_length=1000000,choices=CITY_LIST)
    email_ID=models.EmailField()
    website=models.URLField(max_length=1000000)
    contact_number=models.CharField(max_length=12,default='None')

    def __str__(self):
        return self.supplier_name