from django.shortcuts import render
from django.http import HttpResponse

from order.models import Order
from order.forms import OrderForm

def create_order(request):
    if request.method == 'GET':
        context = {
            'form': OrderForm()
        }

        return render(request, 'order/create_order.html', context=context)

    elif request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            Order.objects.create(
                client=form.cleaned_data['client'],
                product=form.cleaned_data['product'],
                #creation_time=form.cleaned_data['creation_time'],
            )
            context = {
                'message': 'Orden creada exitosamente'
            }
            return render(request, 'order/create_order.html', context=context)
        else:
            context = {
                'form_errors': form.errors,
                'form': OrderForm()
            }
            return render(request, 'order/create_order.html', context=context)

def list_orders(request):
    if 'search' in request.GET:
        search = request.GET['search']
        orders = Order.objects.filter(name__icontains=search)
    else:
        orders = Order.objects.all()
    context = {
        'order':orders,
    }
    return render(request, 'order/list_order.html', context=context)


