from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from .forms import IndexCardForm


class HomePageView(View):
    def get(self, request):
        return(HttpResponse("putanginamo"))


def index_card_view(request):
	if request.method == 'POST':
		form = IndexCardForm(request.POST)
		if form.is_valid():
			return HttpResponse(
				'Hello, {}! Today is going to be a great day!'.format(
					form.cleaned_data['name']
					)
				)
	else:
	    form = IndexCardForm()
	return render(request, 'index.html', {'form': form})