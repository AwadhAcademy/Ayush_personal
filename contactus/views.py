from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import contact

#front Python part()
def contactus(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        phone=request.POST.get('phone')
        data=contact(name=name,email=email,message=message,phone=phone)
        data.save()
    return render(request,'contactus/contactus.html')

