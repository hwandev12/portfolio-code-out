from django.shortcuts import render, reverse
from .forms import CreateUserForm

# create sign up view
def signup(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    return render(request, 'registration/signup.html', {"form": form})
