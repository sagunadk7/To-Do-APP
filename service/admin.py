from django.contrib import admin
from service.models import Services
class AdminPanel(admin.ModelAdmin):
    Display_list = ('task','date')
    
admin.site.register(Services,AdminPanel,)    


# Register your models here.
