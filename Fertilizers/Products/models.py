from django.db import models
class Login(models.Model):
	username = models.CharField(max_length=20, unique=True)
	password = models.CharField(max_length=20)

	def __unicode__(self):
		return self.username
class Customer(models.Model):
    Login_Name=models.CharField(max_length=20)
    Full_Name=models.CharField(max_length=20)
    Password=models.CharField(max_length=10)
    Phone_Number=models.IntegerField()

class Stock_details(models.Model):
	Product_name=models.CharField(max_length=20)
	Manfacturing_date=models.CharField(max_length=20)
	Expire_date=models.CharField(max_length=20)
	Net_weigth=models.CharField(max_length=20)
	Price=models.IntegerField()
	Quantity=models.IntegerField()
	Remarks=models.CharField(max_length=50)

  

# Create your models here.
