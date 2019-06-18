# urls.py
from django.urls import path
from .views import UserCreateView, UserUpdateView, UserDelete

from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('create', UserCreateView.as_view(), name='create_user'),
    path('delete/<int:pk>', UserDelete.as_view(), name='delete_user'),
    path('update/<int:pk>', UserUpdateView.as_view(), name='update_user'),

]
