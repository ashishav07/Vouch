from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name = 'home'),
    path('accounts/', include('allauth.urls')),
    path('mlogin',views.mlogin, name = 'dashboard'),
    path('logout',views.mlogout,name = 'logout')
]
