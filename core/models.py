from django.db import models
from .choices import CRIME_CATEGORY , STATUS
# Create your models here.
class AddComplaint(models.Model):
    name = models.CharField(max_length=60)
    username = models.CharField(max_length=4000)
    mobile_no = models.IntegerField()
    title = models.CharField(max_length=6000)
    city = models.CharField(max_length=100)
    reported_date = models.DateTimeField(auto_now_add=True,blank=True)
    category = models.IntegerField(choices=CRIME_CATEGORY,default=1)
    description =models.CharField(max_length=6000)
    status = models.IntegerField(choices=STATUS,default=1)

