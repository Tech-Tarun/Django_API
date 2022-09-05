from pyexpat import model
from django.db import models

class CartItem(models.Model):
    product_name=models.CharField(max_length=200)
    product_price=models.FloatField()
    product_quantity=models.PositiveIntegerField()

class CCBoard(models.Model):
    cust_name=models.CharField(max_length=200)
    add=models.CharField(max_length=400)
    mobile=models.BigIntegerField()
    card_no=models.BigIntegerField()
    card_limit=models.BigIntegerField()
    card_expiry=models.CharField(max_length=200)
    email=models.CharField(max_length=200)


class admin_login(models.Model):
    user_name=models.CharField(max_length=200)
    pswrd=models.CharField(max_length=200)