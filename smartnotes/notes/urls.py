from django.urls import path

from . import views

app_name = 'notes'

urlpatterns = [
    path('', views.notes_list, name='notes_list_basic'),
    path('<int:pk>/', views.notes_detail, name='notes_detail_basic'),
    path('g/', views.NotesListView.as_view(), name='notes_list'),
    path('g/<int:pk>/', views.NotesDetailView.as_view(), name='notes_detail'),
]