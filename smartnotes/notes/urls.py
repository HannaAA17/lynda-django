from django.urls import path

from . import views

app_name = 'notes'

urlpatterns = [
    path('', views.notes_list, name='notes_list_basic'),
    path('<int:pk>/', views.notes_detail, name='notes_detail_basic'),
]