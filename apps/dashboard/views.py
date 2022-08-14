from django.shortcuts import render
from django.contrib.auth import get_user_model
from apps.portfolio.models import Post
from apps.portfolio.models import Contact

Users = get_user_model()

def dashboard(request):
	users = Users.objects.count()
	posts = Post.objects.count()
	contact = Contact.objects.count()
	contact_objects = Contact.objects.all()
	all_users = Users.objects.all()
	context = {
		"users": users,
	 	"posts": posts,
	  	"contact": contact,
	  	"all_users": all_users,
	  	"contact_objects": contact_objects
	}
	return render(request, 'dashboard/pages/dashboard.html', context)