from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'pigma'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pigma.urls')),
    path('index',views.index),
]