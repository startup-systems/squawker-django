from django.contrib import admin
from .models import Squawk


class SquawkAdmin(admin.ModelAdmin):
    list_display = ('message', 'time')
    
# Register your models here.
admin.site.register(Squawk, SquawkAdmin)


