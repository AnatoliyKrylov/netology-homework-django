from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_method = request.GET.get('sort', 'name')
    if sort_method == 'name':
        phones = Phone.objects.all().order_by('name')
    elif sort_method == 'min_price':
        phones = Phone.objects.all().order_by('price')
    elif sort_method == 'max_price':
        phones = Phone.objects.all().order_by('-price')
    context = {
        'phones': phones
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {
        'phone': phone
    }
    return render(request, template, context)
