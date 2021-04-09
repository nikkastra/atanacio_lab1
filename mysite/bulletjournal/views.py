from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .forms import *
from .models import *


name_dict = {}
#oh la la wow wow wee wa king in the castle king in the castle i have a chair i
#have a chair o go to this go to this hey king in the castle


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
	this_dict = {}
	new_task = ''
	if request.method == 'POST':
		form1 = Task(request.POST)
		form2 = EditTask(request.POST)
		if form1.is_valid() or form2.is_valid():
			x = ''
			for y in request.POST:
				x = y
			if x == 'task':
				new_task = Tasks(name=Name.objects.get(name=name_dict['name']), key=form1.cleaned_data['key'], task=form1.cleaned_data['task'])
				new_task.save()
				the_tasks = [str(x) for x in Tasks.objects.all()]
				this_dict['form1'] = form1
				this_dict['form2'] = form2
				this_dict['the_tasks'] = the_tasks
				return render(request, 'thisweek.html', this_dict)
			elif x == 'edittask':
				new_task.task = request.POST['edittask']
				new_task.save()
				the_tasks = [str(x) for x in Tasks.objects.all()]
				this_dict['form1'] = form1
				this_dict['form2'] = form2
				this_dict['the_tasks'] = the_tasks
				return render(request, 'thisweek.html', this_dict)
	else:
		form1 = Task()
		form2 = EditTask()
		the_tasks = [str(x) for x in Tasks.objects.all()]
		this_dict['form1'] = form1
		this_dict['form2'] = form2
		this_dict['the_tasks'] = the_tasks
	return render(request, 'thisweek.html', this_dict)


def today(request):
	return render(request, 'today.html')