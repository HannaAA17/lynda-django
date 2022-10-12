from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, ListView, DetailView

from . import models, forms


# Create your views here.
def notes_list(request):
    all_notes = models.Note.objects.all()
    return render(request, 'notes/notes_list.html', {'notes':all_notes})


def notes_detail(request, pk):
    note = get_object_or_404(models.Note, pk=pk)
    return render(request, 'notes/notes_detail.html', {'note':note})


class NoteListView(ListView):
    model = models.Note
    context_object_name = "notes" # default: "note_list" or "object_list"
    # template_name = "notes/note_list.html"


class NoteDetailView(DetailView):
    model = models.Note
    # context_object_name = "note" # default: "note" or "object"
    # template_name = "notes/note_detail.html"


class NoteCreateView(CreateView):
    model = models.Note
    # template_name = "notes/note_form.html"
    # fields = ['title', 'text']
    form_class = forms.NotesForm
    success_url = '/notes/g'


# resources
# objects get saved in "object_list" or "(lowercased-model name)_list"
# https://docs.djangoproject.com/en/4.1/topics/class-based-views/generic-display/#making-friendly-template-contexts