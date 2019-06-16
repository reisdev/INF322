from django.db import models

# Create your models here.

class Address(models.Model):
    address_id = models.AutoField(primary_key=True)
    num = models.IntegerField()
    street = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=15)
    zip_code = models.CharField(max_length=20)
    extra_information = models.CharField(blank=True, max_length=512)

class Phone(models.Model):
    phones_id = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=13)

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    nickname = models.CharField(max_length=20)
    addresses = models.ForeignKey(Address, on_delete=models.CASCADE)
    phones = models.ManyToManyField(Phone)

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

class Sale(models.Model):
    sale_id = models.AutoField(primary_key=True)
    done = models.BooleanField()
    initial_price = models.IntegerField()
    duration = models.IntegerField(default=15)
    post_date = models.DateTimeField()
    item = models.ForeignKey(Item, on_delete=models.PROTECT)

class Bid(models.Model):
    bid_id = models.AutoField(primary_key=True)
    value = models.DecimalField(max_digits=10,decimal_places=2)
    time_stamp = models.DateTimeField()

class AuctionSale(Sale):
    bids = models.ForeignKey(Bid, on_delete=models.CASCADE)

class Exchange(Sale):
    pass

class Donation(Sale):
    pass

class Services(Sale):
    pass