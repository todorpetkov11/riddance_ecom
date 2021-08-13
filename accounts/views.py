from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from accounts.forms import UserLoginForm, UserRegisterForm, RiddanceProfileForm
from accounts.models import RiddanceProfile, RiddanceUser
from products.models import ProductModel


def login_user(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('browse')
    else:
        form = UserLoginForm()
    context = {
        'form': form
    }
    return render(request, 'account_templates/user_login.html', context)


def register_user(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('edit profile', pk=request.user.pk)
    else:
        form = UserRegisterForm()
    context = {
        'form': form
    }
    return render(request, 'account_templates/user_register.html', context)


def logout_user(request):
    logout(request)
    return redirect('landing')


@login_required
def profile_details(request, pk):
    profile = RiddanceProfile.objects.get(pk=pk)
    user_products = ProductModel.objects.filter(user_id=pk)
    is_owner = False
    if profile.user == request.user:
        is_owner = True
    context = {
        'products': user_products,
        'profile': profile,
        'is_owner': is_owner
    }
    return render(request, 'profile_templates/profile_details.html', context)


"""
        Goes to the authenticated user's profile page.
"""


@login_required()
def edit_profile(request, pk):
    profile = RiddanceProfile.objects.get(pk=pk)
    if request.method == "POST":
        form = RiddanceProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details', pk=request.user.pk)
    else:
        form = RiddanceProfileForm(instance=profile)

    context = {
        'form': form,
        'profile': profile
    }
    return render(request, 'profile_templates/edit_profile.html', context)


"""
        Goes to the editing form of the authenticated user's profile.
"""


@login_required()
def delete_account(request, pk):
    profile = RiddanceProfile.objects.get(pk=pk)
    account = RiddanceUser.objects.get(pk=pk)
    if request.method == "POST":
        logout(request)
        account.delete()
        profile.delete()
        return redirect('browse')
    else:
        return render(request, 'account_templates/delete_account.html', {'profile': profile})
