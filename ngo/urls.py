
from django.contrib import admin
from django.urls import path, include
from django.conf import settings 
from django.conf.urls.static import static 
from django.contrib.auth import views as auth_views
from user.views import SignUp, login_success


urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'user/', include('user.urls')),
    path(r'event/', include('event.urls')),
    # path(r'event/userview', include('event.urls')),
    path('register/', include('register.urls')),
    path(r'',auth_views.LoginView.as_view(template_name='registration/login.html'),
        name ='login_root'),
    path(r'login/',auth_views.LoginView.as_view(template_name='registration/login.html'),
        name ='login'),
    path(r'logout/', 
        auth_views.LogoutView.as_view(template_name='registration/login.html'), 
        name ='logout'),
    path('signup/', SignUp.as_view(), name ='signup' ),
    path('login_success/', login_success, name ='login_success' ),

    
    # path('register/', include('register.urls')),



]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                                document_root = settings.MEDIA_ROOT)
