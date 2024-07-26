from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class futsal_court(models.Model):
    futsal_court_id=models.AutoField(primary_key=True)
    futsal_name=models.CharField(max_length=50)
    futsal_court_phone=models.CharField(max_length=10)
    futsal_court_address=models.CharField(max_length=50)
    price_per_hour = models.DecimalField(max_digits=6, decimal_places=2)
class Profile(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    phone=models.CharField(max_length=10)

    def __str__(self):
        return str(self.user)
class booking(models.Model):
    booking_id=models.AutoField(primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    start_time=models.DateTimeField()
    duration = models.PositiveIntegerField()