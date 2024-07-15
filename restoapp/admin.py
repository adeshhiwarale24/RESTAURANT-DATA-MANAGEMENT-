from django.contrib import admin
from restoapp.models import resto,dish

class restoAdmin(admin.ModelAdmin):
    list_display = ['rid','name','location','items','lat_long','full_details']
class dishAdmin(admin.ModelAdmin):
    list_display = ['did','dish','mrp']


# Register your models here.
admin.site.register(resto,restoAdmin)
admin.site.register(dish,dishAdmin)
