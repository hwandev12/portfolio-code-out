from django.shortcuts import render, reverse, redirect
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout

# create sign up view
def signup(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Account was created for " + user)
            return redirect("/login/")
    return render(request, 'registration/signup.html', {"form": form})


def login(request):


    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect("/home/")
        else:
            messages.info(request, "Username or Password you entered is wrong!")

    return render(request, 'registration/login.html')
