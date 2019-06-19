from django.urls import path
from . import views

app_name='register'
urlpatterns = [
    path('create/', views.register_create, name='register_create'),
    path('create/(<event_id>\d+)/', views.register_create, name='register_create'),
    path('confirm//(<register_id>\d+)/', views.confirm, name='confirm'),
]
