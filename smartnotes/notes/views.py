from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from . import models


# Create your views here.
def notes_list(request):
    all_notes = models.Notes.objects.all()
    return render(request, 'notes/notes_list.html', {'notes':all_notes})


def notes_detail(request, pk):
    note = get_object_or_404(models.Notes, pk=pk)
    return render(request, 'notes/notes_detail.html', {'note':note})


class NotesListView(ListView):
    model = models.Notes
    context_object_name = "notes" # default: "notes_list" or "object_list"
    template_name = "notes/notes_list.html"


class NotesDetailView(DetailView):
    model = models.Notes
    context_object_name = "note" # default: "notes" or "object"
    template_name = "notes/notes_detail.html"


# resources
# objects get saved in "object_list" or "(lowercased-model name)_list"
# https://docs.djangoproject.com/en/4.1/topics/class-based-views/generic-display/#making-friendly-template-contexts