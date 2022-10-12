from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from datetime import datetime


# Create your views here.
def home_1(request):
    return HttpResponse('<h1> my first app </h1>')


@login_required(login_url='/admin')
def home_2(request):
    return render(request, 'home/welcome.html', {'today': datetime.today()})


class HomeView(LoginRequiredMixin, TemplateView):
    login_url='/admin'
    template_name = 'home/welcome.html'
    extra_context = {'today': datetime.today()}
