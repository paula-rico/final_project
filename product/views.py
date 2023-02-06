from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DeleteView, UpdateView

from product.models import Product
from product.forms import ProductForm



def create_product(request):
    if request.method == 'GET':
        context = {
            'form': ProductForm()
        }

        return render(request, 'product/create_product.html', context=context)

    elif request.method == 'POST':
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            Product.objects.create(
                name=form.cleaned_data['name'],
                price=form.cleaned_data['price'],
                category=form.cleaned_data['category'],
                profile_picture=form.cleaned_data['profile_picture']
            )
            context = {
                'message': 'Producto creado exitosamente'
            }
            return render(request, 'product/create_product.html', context=context)
        else:
            context = {
                'form_errors': form.errors,
                'form': ProductForm()
            }
            return render(request, 'product/create_product.html', context=context)

def list_products(request):
    if 'search' in request.GET:
        search = request.GET['search']
        products = Product.objects.filter(name__icontains=search)

    else:
        products = Product.objects.all()
    context = {
        'product':products,
    }
    return render(request, 'product/list_products.html', context=context)


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product/product-delete.html'
    success_url = '/product/list-products/'




class ProductUpdateView(UpdateView):
    model = Product
    fields = '__all__'
    template_name = 'product/product-update.html'
    success_url = '/product/list-products/'


