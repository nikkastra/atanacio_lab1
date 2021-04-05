from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from .forms import *

name_dict = {}

class HomePageView(View):
    def get(self, request):
    	form = IndexCardForm()
    	return render(request, 'base.html', {'form': form})

def index_card_view(request):
	global name_dict
	if len(name_dict) == 1:
		return render(request, 'base.html', name_dict)
	elif request.method == 'POST':
		form = IndexCardForm(request.POST)
		if form.is_valid():
			name_dict['name'] = form.cleaned_data['name']
			return render(request,'base.html', name_dict)
	else:
	    form = IndexCardForm()
	return render(request, 'base.html', {'form': form})


def profile(request):
	return render(request, 'profile.html')


def key(request):
	return render(request, 'key.html')


def thisweek(request):
	return render(request, 'thisweek.html')


def today(request):
	return render(request, 'today.html')