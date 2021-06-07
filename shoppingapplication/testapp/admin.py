from django.contrib import admin

# Register your models here.
from testapp.models import goods,cart
class admin_goods(admin.ModelAdmin):
    list_display=["gname","gseller","gprice","gquantity"]
admin.site.register(goods,admin_goods)
class admin_cart(admin.ModelAdmin):
    list_display=["user_id","gname","gprice","gquantity"]
admin.site.register(cart,admin_cart)    
