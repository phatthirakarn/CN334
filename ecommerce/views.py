from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ecommerce_index_view(request):
    '''This function render index page of ecommerce views'''
    return HttpResponse('Welcome to 6410742453 Phatthira Karn views!')

def item_view(request, item_id):
    context_data = {
        "item_id": item_id
    }
    return render(request, 'index.html', context= context_data)

def homepage_view(request):
    return render(request, 'homepage.html')

def category_page_view(request):
    return render(request, 'category_page.html')

def product_page_view(request):
    return render(request, 'product_page.html')

def checkout_page_view(request):
    return render(request, 'checkout_page.html')

def contact_page_view(request):
    return render(request, 'contact_page.html')