from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView


class HomeView(TemplateView):
	template_name = 'home.html'


class TextListView(ListView):
	model = None 


class TaskCreateView(CreateView):
	template_name_suffix = '_create_form'