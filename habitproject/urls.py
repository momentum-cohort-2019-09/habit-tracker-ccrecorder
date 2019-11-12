from django.contrib import admin
from django.urls import path, include
from goalkeeper import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('goalkeeper.urls')),
    path('accounts/', include('registration.backends.default.urls')),
    path('', views.index, name="dashboard"),
    path('goalkeeper/create-goal/', views.create_goal, name="create-goal"),
    path('goalkeeper/<int:pk>/display-goal/', views.display_goal, name="display-goal"),
    path('goalkeeper/<int:pk>/edit-goal/', views.edit_goal, name="edit-goal"),

]