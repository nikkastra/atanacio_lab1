from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from .forms import IndexCardForm

class HomePageView(View):
    def get(self, request):
    	form = IndexCardForm()
    	return render(request, 'index.html', {'form': form})


def index_card_view(request):
	if request.method == 'POST':
		form = IndexCardForm(request.POST)
		if form.is_valid():
			return HttpResponse(
				'Hello, {}! Today is gonna be a great day!'.format(
					form.cleaned_data['name']
					)
				)
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