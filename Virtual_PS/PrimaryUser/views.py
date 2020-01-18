from django.shortcuts import render
from django.views.generic import (TemplateView)
# Create your views here.

class PrimaryUserView(TemplateView):
    template_name = 'PrimaryUser/index.html'
    