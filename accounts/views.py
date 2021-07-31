from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from accounts.forms import UserLoginForm, UserRegisterForm, RiddanceProfileForm
from accounts.models import RiddanceProfile
from products.models import ProductModel


def login_user(req):
    if req.method == "POST":
        form = UserLoginForm(req.POST)
        if form.is_valid():
            user = form.save()
            login(req, user)
            return redirect('index')
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
            return redirect('index')
    else:
        form = UserRegisterForm()
    context = {
        'form': form
    }
    return render(req, 'account_templates/user_register.html', context)


def logout_user(req):
    logout(req)
    return redirect('index')


@login_required
def profile_details(req):
    profile = RiddanceProfile.objects.get(pk=req.user.id)
    if req.method == "POST":
        form = RiddanceProfileForm(req.POST, req.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')
    else:
        form = RiddanceProfileForm()

    user_products = ProductModel.objects.filter(user_id=req.user.id)
    context = {
        'form': form,
        'products': user_products,
        'profile': profile,
    }
    return render(req, 'profile_templates/profile_details.html', context)
