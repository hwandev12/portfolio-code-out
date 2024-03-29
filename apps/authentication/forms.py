from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Profile

User = get_user_model()


class CreateUserForm(UserCreationForm):

	class Meta:
		model = User
		username = None
		fields = ["first_name", "last_name", "email", "password1", "password2"]

class UserUpdateForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ["first_name", "last_name", "email"]

class UpdateProfileForm(forms.ModelForm):

	class Meta:
		model = Profile
		fields = ["image"]