from django.shortcuts import render
from comments.models import Comment
# Create your views here.
def product_detail(request, product_id):
    comments = Comment.objects.filter(product_id=product_id)
    return render(request, 'products/detail.html', {'comments':comments})
