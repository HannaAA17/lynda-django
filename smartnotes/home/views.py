from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm

from datetime import datetime


# Create your views here.
def home_1(request):
    return HttpResponse('<h1> my first app </h1>')


@login_required(login_url='/login')
def home_2(request):
    return render(request, 'home/welcome.html', {'today': datetime.today()})


class HomeView(LoginRequiredMixin, TemplateView):
    login_url='/login'
    template_name = 'home/welcome.html'
    extra_context = {'today': datetime.today()}


class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'


class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'


class SignupInterfaceView(CreateView):
    form_class = UserCreationForm
    template_name = 'home/register.html'
    success_url = '/notes/g'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('notes:note_list')
        return super().get(request, *args, **kwargs)