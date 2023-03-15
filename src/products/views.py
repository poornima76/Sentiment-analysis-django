from django.shortcuts import render
from comments.models import Comment
from products.models import Product

# Create your views here.

def product_details(request):
    product = Product.objects.all()
    return render(request, 'products/product_list.html', {'product':product })


