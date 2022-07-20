from multiprocessing import context
from django.shortcuts import render
from . import models

def home(request):
    homeContents = models.Home.objects.all()
    posts = models.Post.objects.all()
    context = {"homeContents": homeContents, "posts": posts}
    return render(request, 'pages/home.html', context)
