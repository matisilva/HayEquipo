#from django.http import HttpResponse
#from django.shortcuts import render_to_response
#from django.template import RequestContext, loader
from django import forms
from django.views.generic import ListView
from django.utils.translation import ugettext as _
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .models import Question

class Home(TemplateView):
    template_name = 'home.html'

    @classmethod
    def as_view(cls, **initkwargs):
        view = super(Home, cls).as_view(**initkwargs)
        return (view)

class QuestionDetailView(DetailView):
    model = Question

