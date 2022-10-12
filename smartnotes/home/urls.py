from django.urls import path

from . import views

app_name = 'home'

urlpatterns = [
    path('home_1/', views.home_1),
    path('home_2/', views.home_2),
]
