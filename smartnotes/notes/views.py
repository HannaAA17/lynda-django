from django.shortcuts import render, get_object_or_404
from . import models

# Create your views here.
def notes_list(request):
    all_notes = models.Notes.objects.all()
    return render(request, 'notes/notes_list.html', {'notes':all_notes})

def notes_detail(request, pk):
    note = get_object_or_404(models.Notes, pk=pk)
    return render(request, 'notes/notes_detail.html', {'note':note})