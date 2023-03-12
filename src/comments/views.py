
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Comment
from .forms import CommentForm
from products.models import Product
from profiles.models import Profile
from django.http import HttpResponse
from .inference_pipe import predict
import joblib
import os

from django.conf import settings
path_to_model = os.path.join(settings.BASE_DIR, "model/")
classifier = joblib.load(open(path_to_model + "pipeline.joblib", "rb"))

def create_comment(request, product_id):
    product = Product.objects.get(pk= int(product_id))
    profile = Profile.objects.get(pk=2)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.product = product
            comment.profile = profile
            comment.prediction = classifier.predict([comment.text])[0] 
            comment.save()
            
            # return redirect('product_detail', product_id=product.pk)
            return HttpResponse(messages.success(request, 'Comment added successfully'))
    else:
        form = CommentForm()
    return render(request, 'comments/create_comment.html', {'form': form, 'product': product})

def delete_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    if request.user == comment.profile.user:
        comment.delete()
        messages.success(request, 'Comment deleted successfully')
    else:
        messages.error(request, 'You do not have permission to delete this comment')
    return redirect('product_detail', product_id=comment.product.id)


# id=product_id
#pk=1