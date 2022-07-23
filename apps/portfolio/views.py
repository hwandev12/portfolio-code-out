from multiprocessing import context
from django.shortcuts import render
from . import models

def home(request):
    homeContents = models.Home.objects.all()
    posts = models.Post.objects.all()
    context = {"homeContents": homeContents, "posts": posts}
    return render(request, 'pages/home.html', context)

# for single web page
def post(request, pk):
    post = models.Post.objects.get(id=pk)
    context = {"post": post}
    return render(request, 'pages/post.html', context)

# for category page cards
def category(request):
    return render(request, 'pages/category_cards.html')