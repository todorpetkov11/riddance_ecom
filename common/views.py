from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView
from cart.views import get_cart
from common.forms import OrderForm
from common.models import Order
from products.models import ProductModel


class BrowseView(ListView):
    model = ProductModel
    paginate_by = 8
    template_name = "browsing/index.html"


class SearchResultsView(ListView):
    model = ProductModel
    template_name = 'browsing/search.html'

    def get_queryset(self):
        query = self.request.GET.get('query')
        object_list = ProductModel.objects.filter(
            Q(name__icontains=query) | Q(category__icontains=query)
        )
        return object_list


def browse_category(request, category):
    if category:
        products = ProductModel.objects.filter(category=category)
    else:
        products = ProductModel.objects.all()
    context = {'products': products}
    return render(request, 'browsing/category_search.html', context)


class LandingView(TemplateView):
    template_name = 'landing.html'


def checkout(request):
    cart = get_cart(request)
    items = cart.items.all()
    if request.method == "POST":
        for item in items:
            form = OrderForm(request.POST)
            if form.is_valid():
                order = form.save(commit=False)
                order.receiver = item.product.user
                order.sender = request.user
                order.product = item.product
                order.save()
                cart.items.remove(item)
        return render(request, 'orders_and_checkout/successful_order.html')

    else:
        form = OrderForm
        return render(request, 'orders_and_checkout/checkout.html', {'form': form, 'cart': cart, 'items': items})


def orders_details(request):
    orders = Order.objects.filter(receiver=request.user)
    context = {
        'orders': orders,
    }
    return render(request, 'orders_and_checkout/orders.html', context)


def accept_order(request, pk):
    order = Order.objects.get(pk=pk)
    product = order.product
    product.delete()
    order.delete()
    return redirect('orders')


def dismiss_order(request, pk):
    order = Order.objects.get(pk=pk)
    order.delete()
    return redirect('orders')
