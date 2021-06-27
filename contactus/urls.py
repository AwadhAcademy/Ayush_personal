from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('contactus',views.contactus,name="contactus"),
    # path("insta",views.insta,name="insta"),
]
