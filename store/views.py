from django.shortcuts import render
from django.http import HttpResponse

from store.models import Stores
from store.forms import StoreForm

def create_store(request):
    if request.method == 'GET':
        context = {
            'form': StoreForm()
        }

        return render(request, 'store/create_store.html', context=context)

    elif request.method == 'POST':
        form = StoreForm(request.POST)
        if form.is_valid():
            Stores.objects.create(
                name=form.cleaned_data['name'],
                address=form.cleaned_data['address'],
                city=form.cleaned_data['city'],
                region=form.cleaned_data['region'],
                postal_code=form.cleaned_data['postal_code'],
            )
            context = {
                'message': 'Tienda creada exitosamente'
            }
            return render(request, 'store/create_store.html', context=context)
        else:
            context = {
                'form_errors': form.errors,
                'form': StoreForm()
            }
            return render(request, 'store/create_store.html', context=context)

def list_stores(request):
    if 'search' in request.GET:
        search = request.GET['search']
        stores = Stores.objects.filter(name__icontains=search)
    else:
        stores = Stores.objects.all()
    context = {
        'store':stores,
    }
    return render(request, 'store/list_stores.html', context=context)


