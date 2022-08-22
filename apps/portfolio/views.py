from django.shortcuts import redirect, render
from . import models
from .forms import ContactUsModelForm

# rest frameworks
from rest_framework import viewsets
from .serializers import ContactSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import generics


# class ContactListCreateApiView(generics.ListCreateAPIView):
#     queryset = models.Contact.objects.all()     
#     serializer_class = ContactSerializer

#     def create_list(self, serializer):
#         your_name = serializer.validated_data.get("your_name")
#         last_name = serializer.validated_data.get("last_name")
#         message = serializer.validated_data.get("message") or None

#         if message is None:
#             message = your_name
#         # serializer.save(message=message)

# contact_list_create_view = ContactListCreateApiView.as_view()





# API userset
@api_view(["GET"])
def contact_api(request):
    api_urls = {
        "List": "/contact-list/",
        "Detail View": "/contact-detail/<str:pk>/",
        "Create": "/contact-create/",
        "Update": "/contact-update/<str:pk>/",
        "Delete": "/contact-delete/<str:pk>",
    }

    return Response(api_urls)




def home(request):
    homeContents = models.Home.objects.all()
    # It is how we limit to get the data from database
    posts = models.Post.objects.all().order_by('id')[:3]
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


# about us page
def about(request):

    return render(request, 'pages/about.html')

# create 404 page
def error_500(request):

    return render(request, 'pages/500.html', status=500)


# create 404 page
def error_404(request, exception):

    return render(request, 'pages/404.html', status=404)


# create contact us page
def contact(request):
    if request.method == "POST":
        form = ContactUsModelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    else:
        form = ContactUsModelForm()

    return render(request, 'pages/contact.html', {"form": form})