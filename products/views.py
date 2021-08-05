from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory, inlineformset_factory
from django.shortcuts import render, redirect

from cart.models import Cart
from cart.views import get_cart
from products.forms import ImageForm, ProductForm
from products.models import ImageModel, ProductModel


@login_required()
def add_product(request):
    image_form_set = modelformset_factory(
        model=ImageModel, form=ImageForm, fields=('image',), max_num=3, extra=3)

    if request.method == 'POST':
        product_form = ProductForm(
            request.POST, request.FILES)
        formset = image_form_set(
            request.POST, request.FILES)
        if product_form.is_valid() and formset.is_valid():
            product = product_form.save(commit=False)
            product.user = request.user
            product.save()
            for form in formset.cleaned_data:
                if form:
                    image = form['image']
                    photo = ImageModel(product=product, image=image)
                    photo.save()
        return redirect('browse')
    else:
        product_form = ProductForm()
        formset = image_form_set(queryset=ImageModel.objects.none())
        context = {'product_form': product_form, 'formset': formset}
        return render(request, 'product_templates/add_product.html', context)


@login_required()
def edit_product(request, pk):
    product_to_edit = ProductModel.objects.get(pk=pk)
    ImageFormSet = inlineformset_factory(parent_model=ProductModel, model=ImageModel, form=ImageForm,
                                         max_num=3, fields=('image',))

    if request.method == 'POST':
        product_form = ProductForm(
            request.POST, request.FILES, instance=product_to_edit)
        formset = ImageFormSet(
            request.POST, request.FILES, instance=product_to_edit)
        if product_form.is_valid() and formset.is_valid():
            product = product_form.save(commit=False)
            product.user = request.user
            product.save()
            formset.save()
            return redirect('profile details')
    else:
        product_form = ProductForm(instance=product_to_edit)
        formset = ImageFormSet(instance=product_to_edit)
        context = {'product_form': product_form, 'formset': formset, 'product': product_to_edit}
        return render(request, 'product_templates/edit_product.html', context)


@login_required()
def delete_product(request, pk):
    product = ProductModel.objects.get(pk=pk)
    if request.method == "POST":
        product.delete()
        return redirect('profile details')
    else:
        return render(request, 'product_templates/delete_product.html',
                      {'product': product, 'page_name': 'delete product'})


@login_required()
def product_details(request, pk):
    product = ProductModel.objects.get(pk=pk)
    images = ImageModel.objects.filter(product_id=pk)
    is_owner = False

    if product.user == request.user:
        is_owner = True

    context = {'product': product, 'images': images, 'is_owner': is_owner}
    return render(request, 'product_templates/product.html', context)
