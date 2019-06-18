from django.db import models


# Create your models here.

class Address():

    def __init__(self, num, street, district, city, state, zip_code, extra_information):
        self._num = str(num)
        self._street = street
        self._district = district
        self._city = city
        self._state = state
        self._zip_code = str(zip_code)
        self._extra_information = extra_information

    def get_values(self):
        values = "T_ADDRESS(" + "'" + self._num + "'," \
                 + "'" + self._street + "'," \
                 + "'" + self._district + "'," \
                 + "'" + self._city + "')"
        return values


class Phone():
    def __init__(self, phone_list):
        self._phone_list = phone_list

    def get_values(self):
        values = ""
        for i in self._phone_list:
            if len(i) == 1:
                values += "'" + str(self._phone_list) + "'"
                break
            else:
                values += "'" + str(i) + "',"
        return "T_PHONES(" + values + ")"


class User:

    def __init__(self, fullname, email, nickname, addresses, phones, password):
        self._password = password
        self._fullname = fullname
        self._email = email
        self._nickname = nickname
        self._addresses = addresses
        self._phones = phones

    def get_values(self):
        values = "'" + self._email + "'," \
                 + "'" + self._fullname + "'," \
                 + "'" + self._nickname + "'," \
                 + "'" + self._password + "'," \
                 + "" + self._addresses.get_values() + "," \
                 + "" + self._phones.get_values() + ""
        return values

    def get_format(self):
        return "EMAIL, FULLNAME, NICKNAME, PASSWORD, ADDRESSES, PHONES"


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
    value = models.DecimalField(max_digits=10, decimal_places=2)
    time_stamp = models.DateTimeField()


class AuctionSale(Sale):
    bids = models.ForeignKey(Bid, on_delete=models.CASCADE)


class Exchange(Sale):
    pass


class Donation(Sale):
    pass


class Services(Sale):
    pass
