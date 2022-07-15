from django.shortcuts import render

def home(request):
    print("Djang rest world")
    return render(request, 'pages/home.html')
