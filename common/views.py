from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from products.models import ProductModel


class BrowseView(ListView):
    model = ProductModel
    paginate_by = 10
    template_name = "index.html"


class LandingView(TemplateView):
    template_name = 'landing.html'
