from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from . import models, forms


# Create your views here.
def notes_list(request):
    all_notes = models.Note.objects.all()
    return render(request, 'notes/notes_list.html', {'notes':all_notes})


def notes_detail(request, pk):
    note = get_object_or_404(models.Note, pk=pk)
    return render(request, 'notes/notes_detail.html', {'note':note})


class NoteListView(LoginRequiredMixin, ListView):
    login_url = '/login'

    model = models.Note
    context_object_name = "notes" # default: "note_list" or "object_list"
    # template_name = "notes/note_list.html"
    
    def get_queryset(self):
        return self.request.user.notes.all()


class NoteDetailView(LoginRequiredMixin, DetailView):
    login_url = '/login'

    model = models.Note
    # context_object_name = "note" # default: "note" or "object"
    # template_name = "notes/note_detail.html"


class NoteCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login'

    model = models.Note
    # template_name = "notes/note_form.html"
    # fields = ['title', 'text']
    form_class = forms.NotesForm
    success_url = '/notes/g'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['method'] = 'Create New'
        return context
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class NoteUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login'

    model = models.Note
    form_class = forms.NotesForm
    success_url = '/notes/g'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['method'] = 'Edit'
        return context


class NoteDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/login'

    model = models.Note
    success_url = '/notes/g'


# resources
# objects get saved in "object_list" or "(lowercased-model name)_list"
# https://docs.djangoproject.com/en/4.1/topics/class-based-views/generic-display/#making-friendly-template-contexts