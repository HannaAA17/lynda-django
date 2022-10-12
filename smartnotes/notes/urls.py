from django.urls import path

from . import views

app_name = 'notes'

urlpatterns = [

    path('', views.notes_list, name='notes_list_basic'),
    path('<int:pk>/', views.notes_detail, name='notes_detail_basic'),

    path('g/', views.NoteListView.as_view(), name='note_list'),
    path('g/<int:pk>/', views.NoteDetailView.as_view(), name='note_detail'),
    path('g/<int:pk>/edit', views.NotesUpdateView.as_view(), name="note_update"),
    path('g/new/', views.NoteCreateView.as_view(), name='note_new'),

]