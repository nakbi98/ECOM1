from itertools import product
from django.contrib import admin
from .models import Category, Prodect
# Register your models here.
class admincategory(admin.ModelAdmin):
    list_display = ('name', 'date_added')

class adminprodect(admin.ModelAdmin):
    list_display = ('title', 'price', 'category', 'date_add')
admin.site.register(Category,admincategory)
admin.site.register(Prodect,adminprodect)
