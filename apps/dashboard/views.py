from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from apps.portfolio.models import Post
from apps.portfolio.models import Contact
from apps.authentication.forms import CreateUserForm

Users = get_user_model()


def dashboard(request):
    users = Users.objects.count()
    posts = Post.objects.count()
    contact = Contact.objects.count()
    contact_objects = Contact.objects.all()
    all_users = Users.objects.all().order_by('id')[:10]
    complaints = Contact.objects.filter(category__name='Shikoyat').count()
    offers = Contact.objects.filter(category__name='Taklif').count()
    context = {
        "users": users,
        "posts": posts,
        "contact": contact,
        "all_users": all_users,
        "contact_objects": contact_objects,
        "complaints": complaints,
        "offers": offers
    }
    return render(request, 'dashboard/pages/dashboard.html', context)

# create user
def create_user(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/dashboard/")
    return render(request, 'dashboard/pages/create_user.html', {"form": form})