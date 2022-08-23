from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Profile(models.Model):
	user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
	image = models.ImageField(default="default.png", upload_to='profile_pictures')

	def __str__(self):
		return f"{self.user.username} Profile"