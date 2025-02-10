from django.contrib import admin
from django.urls import path
from home import views
from django.urls import path
from .views import generate_certificate


urlpatterns = [
    path('',views.index,name='home'),
    path('about',views.about,name='about'),
    path('services',views.services,name='services'),
    path('contact',views.contact,name='contact'),
    path("certificate/", generate_certificate, name="certificate"),

]


