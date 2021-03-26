from django.db import models

# Create your models here.


class Product(models.Model):
    Product_id = models.AutoField
    Product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    sub_category = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.Product_name


class Signup(models.Model):
    username = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    password = models.CharField(max_length=12)
    Cn_password = models.CharField(max_length=12)

    def __str__(self):
        return self.username


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=90)
    last_name = models.CharField(max_length=90)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=111)
    address_1 = models.CharField(max_length=111)
    address_2 = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111)

    def __str__(self):
        return self.email


class Contact(models.Model):

    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    subject = models.CharField(max_length=122)
    message = models.CharField(max_length=300)

    def __str__(self):
        return self.email
