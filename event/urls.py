from django.urls import path
# from .views import UserCreateView, UserUpdateView, UserDelete

from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('create', views.EventCreateView.as_view(), name='event-create'),
    path('delete/<int:pk>', views.EventDelete.as_view(), name='event-delete'),
    path('update/<int:pk>', views.EventUpdateView.as_view(), name='event-update'),

]