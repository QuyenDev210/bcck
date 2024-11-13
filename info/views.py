from django.shortcuts import render
from django.http import HttpResponse
from .models import info

# Create your views here.
def list(request):
    Data = {'Info': info.objects.all()}
    return render(request , 'info.html', Data)