from django.contrib import admin
from qingShang.models import *
# Register your models here.
class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ['id','tTitle']
class ShopInfoAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ['id','sTitle','sPrice','sUnit','sStar','sContent']

admin.site.register(TypeInfo,TypeInfoAdmin)
admin.site.register(ShopInfo,ShopInfoAdmin)