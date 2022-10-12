from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from datetime import datetime

# Create your views here.
def home_1(request):
    return HttpResponse('<h1> my first app </h1>')

@login_required(login_url='/admin')
def home_2(request):
    return render(request, 'home/welcome.html', {'today': datetime.today()})