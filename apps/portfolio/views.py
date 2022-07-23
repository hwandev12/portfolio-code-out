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
    categories = models.Category.objects.all()
    context = {
        "categories": categories
    }
    return render(request, 'pages/category_cards.html', context)

# for actual category
def category_pages(request):
   
    category = request.GET.get('category')
    
    if category == None:
        posts = models.Post.objects.all()
    else:
        posts = models.Post.objects.filter(category__name=category)


    categories = models.Category.objects.all()
    context = {
       "posts": posts,
       'categories': categories
    }
    return render(request, 'pages/category_pages.html', context)

