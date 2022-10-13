from django.urls import path

from . import views

app_name = 'home'

urlpatterns = [
    path('home_1/', views.home_1),
    path('home_2/', views.home_2),
    path('home_3/', views.HomeView.as_view()),
    path('login/', views.LoginInterfaceView.as_view(), name='login'),
    path('signup/', views.SignupInterfaceView.as_view(), name='signup'),
    path('logout/', views.LogoutInterfaceView.as_view(), name='logout'),
]
