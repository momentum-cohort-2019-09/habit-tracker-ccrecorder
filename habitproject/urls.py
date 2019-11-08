
from django.contrib import admin
from django.urls import path, include
from goalkeeper import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.default.urls')),
    path('', views.index, name='base'),
    path('api/', include('goalkeeper.urls')),
    
]
