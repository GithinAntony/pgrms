from django.urls import path
from . import views

app_name='index'
urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('feature', views.feature, name='feature'),
    path('team', views.team, name='team'),
    path('contact-us', views.contact_us, name='contact_us'),         
    ]
