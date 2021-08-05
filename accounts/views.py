from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from accounts.forms import UserLoginForm, UserRegisterForm, RiddanceProfileForm, ShippingAddressForm
from accounts.models import RiddanceProfile, ShippingAddress
from products.models import ProductModel


def login_user(req):
    if req.method == "POST":
        form = UserLoginForm(req.POST)
        if form.is_valid():
            user = form.save()
            login(req, user)
            return redirect('browse')
    else:
        form = UserLoginForm()
    context = {
        'form': form
    }
    return render(req, 'account_templates/user_login.html', context)


def register_user(req):
    if req.method == "POST":
        form = UserRegisterForm(req.POST)
        if form.is_valid():
            user = form.save()
            login(req, user)
            return redirect('edit profile')
    else:
        form = UserRegisterForm()
    context = {
        'form': form
    }
    return render(req, 'account_templates/user_register.html', context)


def logout_user(req):
    logout(req)
    return redirect('landing')


@login_required
def profile_details(request):
    profile = RiddanceProfile.objects.get(pk=request.user.id)
    user_products = ProductModel.objects.filter(user_id=request.user.id)
    shipping_address = ShippingAddress.objects.get(user_id=request.user.id)
    context = {
        'products': user_products,
        'profile': profile,
        'shipping_address': shipping_address,
    }
    return render(request, 'profile_templates/profile_details.html', context)


@login_required()
def edit_profile(request):
    profile = RiddanceProfile.objects.get(pk=request.user.id)
    shipping_address = ShippingAddress.objects.get(user_id=request.user.id)
    if request.method == "POST":
        form = RiddanceProfileForm(request.POST, request.FILES, instance=profile)
        shipping_form = ShippingAddressForm(request.POST, instance=shipping_address)
        if form.is_valid() and shipping_form.is_valid():
            form.save()
            shipping_form.save()
            return redirect('profile details')
    else:
        form = RiddanceProfileForm(instance=profile)
        shipping_form = ShippingAddressForm(instance=shipping_address)

    context = {
        'form': form,
        'shipping_form': shipping_form,
        'profile': profile
    }
    return render(request, 'profile_templates/edit_profile.html', context)
