from django.shortcuts import render

# Create your views here.
from django.views import generic
from .forms import userpromptForm

class IndexView(generic.TemplateView):
    template_name = "top.html"


class userpromptview(generic.FormView):
    template_name = "userprompt.html"
    form_class = userpromptForm




    

