from django.db import models

# Create your models here.
class user(models.Model):
    user_id=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    user_phone=models.CharField(max_length=10) 
    password=models.CharField(max_length=128, default='')

class futsal_court(models.Model):
    futsal_court_id=models.AutoField(primary_key=True)
    futsal_name=models.CharField(max_length=50)
    futsal_court_phone=models.CharField(max_length=10)
    futsal_court_address=models.CharField(max_length=50)
    price_per_hour = models.DecimalField(max_digits=6, decimal_places=2)

class booking(models.Model):
    booking_id=models.AutoField(primary_key=True)
    user=models.ForeignKey(user,on_delete=models.CASCADE)
    start_time=models.DateTimeField()
    duration = models.PositiveIntegerField()