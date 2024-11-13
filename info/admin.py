from django.contrib import admin
from .models import info
from django.shortcuts import render

class infoAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'birthday', 'gender', 'phone', 'email']
    list_filter = ['age']
    search_fields = ['name']

admin.site.register(info, infoAdmin)

def list(request):
    Date = {'Info': info.objects.all().order_by('-date')}
    return render(request , 'info/info.html', Date)
