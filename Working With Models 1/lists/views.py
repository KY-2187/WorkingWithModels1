from django.views.generic.base import TemplateView, View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

from django.http import HttpResponse
from dhango.shortcuts import render

class HomeView(View):

	def get(self, request, 'args, ''kwargs):
		return render(request, 'home.html')

	def post(self, request, 'args, ''kwargs):
		return render(request, 'home.html', {
			'new_task': request.POST.get('item_text')
		})


class TextListView(ListView):
	model = None 


class TaskCreateView(CreateView):
	template_name_suffix = '_create_form'


def home_page(request):
	if request.method == 'POST':
		return render(request, 'home.html', {
			'new_task': request.POST.get('item_text')
		})
	return render(request, 'home.html')