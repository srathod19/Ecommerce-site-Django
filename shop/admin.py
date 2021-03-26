from django.contrib import admin
from .models import Product, Signup, Contact, Orders
# Register your models here.

admin.site.register(Product)
admin.site.register(Signup)
admin.site.register(Contact)
admin.site.register(Orders)
