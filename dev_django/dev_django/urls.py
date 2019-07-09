from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/<nome>/<idade>/', views.hello),
    path('soma/<int:num1>/<int:num2>/', views.soma)
]
