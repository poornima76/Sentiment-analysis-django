from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Comment
from .forms import CommentForm
from products.models import Product
from profiles.models import Profile
from django.urls import reverse
from .inference_pipe import predict
import joblib
from matplotlib import pyplot as plt
import os

from django.conf import settings
path_to_model = os.path.join(settings.BASE_DIR, "model/")
classifier = joblib.load(open(path_to_model + "pipeline.joblib", "rb"))

def product_details(request):
    product = Product.objects.all()
    return render(request, 'comments/product_list.html', {'product':product })

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
        return redirect('comments:create_comment', product_id=product_id) 
    else:
        form = CommentForm()
        profile = Profile.objects.get(pk=2)
        comment = Comment.objects.filter(product__pk=product_id)
        ones = comment.filter(prediction = 1).count()
        zeros = comment.filter(prediction = 0).count() 
        print(ones)
        context ={'form': form, 'product': product, 'comment': comment,'profile': profile, 'predictions':{'one':ones, 'zero':zeros}}
    return render(request, 'comments/create_comment.html', context)

def delete_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    if request.user == comment.profile.user:
        comment.delete()
        messages.success(request, 'Comment deleted successfully')
    else:
        messages.error(request, 'You do not have permission to delete this comment')
    return redirect('product_detail', product_id=comment.product.id)
