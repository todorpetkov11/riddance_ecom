from django.shortcuts import render
from django.views.generic import ListView

from products.models import ProductModel


class HomeView(ListView):
    model = ProductModel
    paginate_by = 10
    template_name = "index.html"
