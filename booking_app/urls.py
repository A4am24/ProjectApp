from django.urls import path
# from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hotel_view/', views.hotel_view, name='hotel_view'),
    path('booking/', views.booking, name='booking'),
    path('create_login/', views.create_login, name='create_login'),
    path('enter_login/', views.enter_login, name='enter_login'),
]

