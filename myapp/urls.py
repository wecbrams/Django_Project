from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('gallery/', views.mygallery, name='gallery'),
    path('about/', views.aboutus, name='about'),
    path('contact/', views.contactus, name='contact'),


]
