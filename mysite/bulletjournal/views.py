from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import *
from django.urls import *
from django.shortcuts import redirect

from .forms import *
from .models import *


name_dict = {}
#oh la la wow wow wee wa king in the castle king in the castle i have a chair i
#have a chair o go to this go to this hey king in the castle


class NameListView(ListView):
	model = Name


class TaskDetailView(DetailView):
	model = Tasks


class TaskListView(ListView):
	model = Tasks
	template_name = 'thisweek.html'


class TodayListView(ListView):
	model = Today
	template_name = 'today.html'


class TodayDetailView(DetailView):
	model = Today


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
	global name_dict
	info = Name.objects.get(name=name_dict['name'])
	picture = info.image
	nickname = info.nickname
	bio = info.bio
	if request.method == "POST":
		form1 = Picture(request.POST, request.FILES)
		form2 = Nickname(request.POST)
		form3 = Bio(request.POST)
		if form1.is_valid() or form2.is_valid() or form3.is_valid():
			if len(request.FILES) == 1:
				form1.save()
				test = Name.objects.get(name="test")
				info.image = test.image
				picture = info.image
				info.save()
				test.delete()
				info_dict = {'name': name_dict['name'],'nickname': nickname, 'bio': bio, 'picture':picture, 'form1':form1, 'form2': form2, 'form3':form3}
				return render(request, 'profile.html', info_dict)
			elif len(request.POST) == 2:
				x = ''
				for y in request.POST:
					x = y
				if x == 'nickname':
					info.nickname = request.POST['nickname']
					nickname = info.nickname
					info.save()
					info_dict = {'name': name_dict['name'],'nickname': nickname, 'bio': bio, 'picture':picture, 'form1':form1, 'form2': form2, 'form3':form3}
					return render(request, 'profile.html', info_dict)
				else:
					info.bio = request.POST['bio']
					bio = info.bio
					info.save()
					info_dict = {'name': name_dict['name'],'nickname': nickname, 'bio': bio, 'picture':picture, 'form1':form1, 'form2': form2, 'form3':form3}
					return render(request, 'profile.html', info_dict)
	else:
		form1 = Picture()
		form2 = Nickname(use_required_attribute=False)
		form3 = Bio(use_required_attribute=False)
		info_dict = {'name': name_dict['name'],'nickname': nickname, 'bio': bio, 'picture':picture, 'form1':form1, 'form2': form2, 'form3':form3}
	return render(request, 'profile.html', info_dict)


def key(request):
	key_dict = {}
	if request.method == 'POST':
		form = Keys(request.POST)
		if form.is_valid():
			new_key = Key(key=form.cleaned_data['key'], description=form.cleaned_data['description'])
			new_key.save()
			key_dict = {'form': form}
			the_keys = [str(x) for x in Key.objects.all()]
			key_dict['the_keys'] = the_keys
			return render(request, 'key.html', key_dict)
	else:
		form = Keys()
		key_dict = {'form':form}
		the_keys = [str(x) for x in Key.objects.all()]
		key_dict['the_keys'] = the_keys
	return render(request, 'key.html', key_dict)


def thisweek(request):
	if request.method == 'POST':
		form = Task(request.POST)
		if form.is_valid():
			new_task = Tasks(name=Name.objects.get(name=name_dict['name']), key=form.cleaned_data['key'], task=form.cleaned_data['task'])
			new_task.save()
			return redirect('thisweek')
	else:
		form = Task()
	return render(request, 'addtask.html', {'form': form})

def delete_task(request):
	if request.method == 'POST':
		form = Task(request.POST)
		if form.is_valid():
			the_task.delete()
			return redirect('thisweek')
	else:
		form = Task()
	return render(request, 'task_detail', {'form': form})


def today(request):
	if request.method == 'POST':
		form = Today(request.POST)
		if form.is_valid():
			new_task = Today(name=Name.objects.get(name=name_dict['name']), key=form.cleaned_data['key'], task=form.cleaned_data['task'])
			new_task.save()
			return redirect('today')
	else:
		form = Today()
	return render(request, 'addtoday.html', {'form': form})