from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#front Python part()
def home(request):
    return render(request,'home/basic.html')

