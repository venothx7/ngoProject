from django.urls import path, include
# from .views import UserCreateView, UserUpdateView, UserDelete

from . import views
app_name='event'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('create', views.EventCreateView.as_view(), name='event-create'),
    path('delete/<int:pk>', views.EventDelete.as_view(), name='event-delete'),
    path('update/<int:pk>', views.EventUpdateView.as_view(), name='event-update'),
    path('(<id>\d+)/(<slug>[-\w]+)/', views.register_detail, name='register_detail'),
    path('userview', views.event_list, name='event_list'),      
    # path('register/', include('register.urls')),

]