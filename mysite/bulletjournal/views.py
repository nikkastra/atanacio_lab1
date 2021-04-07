from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .forms import *
from .models import *

name_dict = {}

class NameListView(ListView):
	model = Name


class NameDetailView(DetailView):
	model = Name


class HomePageView(View):
    def get(self, request):
    	form = IndexCardForm()
    	return render(request, 'index.html', {'form': form})

def index_card_view(request):
	global name_dict
	if len(name_dict) == 1:
		return render(request, 'index.html', name_dict)
	elif request.method == 'POST':
		form = IndexCardForm(request.POST)
		if form.is_valid():
			name_dict['name'] = form.cleaned_data['name']
			return render(request,'index.html', name_dict)
	else:
	    form = IndexCardForm()
	return render(request, 'index.html', {'form': form})


def profile(request):
	return render(request, 'profile.html')


def key(request):
	return render(request, 'key.html')


def thisweek(request):
	return render(request, 'thisweek.html')


def today(request):
	return render(request, 'today.html')