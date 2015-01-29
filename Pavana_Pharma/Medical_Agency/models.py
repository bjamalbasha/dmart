from django.db import models

# Create your models here.


class Login(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __unicode__(self):
        return unicode(self.username)


class ComplteStockDetails(models.Model):
    batch_num = models.IntegerField(unique=True)
    item_name = models.CharField(max_length=50, unique=True)
    company = models.CharField(max_length=30)
    price_per_unit = models.FloatField()
    manf_data = models.CharField(max_length=10)
    exp_data = models.CharField(max_length=10)
    quantity = models.CharField(max_length=10)
    comments = models.CharField(max_length=100)

    def __unicode__(self):
        return unicode(self.batch_num)


class DealersInfo(models.Model):
    dealer_name = models.CharField(max_length=50)
    dealer_company_name = models.CharField(max_length=50)
    dealer_addrs = models.CharField(max_length=200)
    dealer_dl1 = models.CharField(max_length=15)
    dealer_dl2 = models.CharField(max_length=15)
    dealer_tin = models.CharField(max_length=15)
    dealer_phone = models.IntegerField()
    dealer_email = models.CharField(max_length=50, blank=True, null=True)

    def __unicode__(self):
        return unicode(self.dealer_name)
