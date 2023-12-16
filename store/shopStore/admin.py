from django.contrib import admin
from .models.product import Product
from .models.category import Category
from  .models.orders import  Order
from .models.customer import Customer 
from .models.subscriber import Subscriber

class AdminProduct(admin.ModelAdmin):
    list_display = ['name','price','category']

class AdminCategory(admin.ModelAdmin):
    list_display = ['name']

# Register your models here.
admin.site.register(Product,AdminProduct)
admin.site.register(Category,AdminCategory)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Subscriber)