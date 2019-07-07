from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Choice,Question


class IndexView(generic.ListView):
	template_name = 'preguntas/index.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		"""Return the last five published questions."""
		return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
	model = Question
	template_name = 'preguntas/detail.html'


class ResultsView(generic.DetailView):
	model = Question
	template_name = 'preguntas/results.html'

	


	
	
