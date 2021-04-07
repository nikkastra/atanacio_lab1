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
    	form = FirstName()
    	return render(request, 'index.html', {'form': form})

def home(request):
	if len(name_dict) == 1:
		return render(request, 'index.html', name_dict)
	elif request.method == 'POST':
		form=FirstName(request.POST)
		if form.is_valid():
			name_dict['name'] = form.cleaned_data['name']
			try:
				if Name.objects.get(name=name_dict['name']) in Name.objects.all():
					return render(request,'index.html', name_dict)
			except:
				person_info = Name(name=name_dict['name'])
				person_info.save()
			return render(request, 'index.html', name_dict)
	else:
	    form = FirstName()
	return render(request, 'index.html', {'form': form})


def profile(request):
	if request.method == 'POST':
		form = NicknameAndBio(request.POST)
		if form.is_valid():
			info = Name.objects.get(name=name_dict['name'])
			info.nickname = form.cleaned_data['nickname']
			info.bio = form.cleaned_data['bio']
			new_info = info.save()
			return redirect('name_detail', pk=new_info)
	else:
		form = NicknameAndBio()
	return render(request, 'profile.html', info_dict)


def key(request):
	return render(request, 'key.html')


def thisweek(request):
	return render(request, 'thisweek.html')


def today(request):
	return render(request, 'today.html')