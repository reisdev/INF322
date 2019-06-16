from django.db import models

# Create your models here.


class Addresses(models.Model):
    address_id = models.AutoField(primary_key=True)
    num = models.IntegerField()
    street = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=15)
    zip_code = models.CharField(max_length=20)
    extra_information = models.CharField(blank=True)


class Phones(models.Model):
    phones_id = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=13)


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    nickname = models.CharField(max_length=20)
    addresses = models.ForeignKey(Addresses, on_delete=models.CASCADE)
    phones = models.ForeignKey(Phones, on_delete=models.CASCADE)


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField()


class Items(models.Model):
    items_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)


class Sales(models.Model):
    sales_id = models.AutoField(primary_key=True)
    done = models.BooleanField()
    initial_price = models.IntegerField()
    duration = models.IntegerField()
    post_date = models.DateTimeField()
    item = models.ForeignKey(Items, on_delete=models.PROTECT)


class Bids(models.Model):
    bids_id = models.AutoField(primary_key=True)
    value = models.DecimalField()
    time_stamp = models.DateTimeField()


class AuctionSale(Sales):
    bids = models.ForeignKey(Bids, on_delete=models.CASCADE)


class Exchange(Sales):
    pass


class Donation(Sales):
    pass


class Services(Sales):
    pass
