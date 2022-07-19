from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
class Home(models.Model):
    class Meta:
        verbose_name = 'Home'
        verbose_name_plural = "Home Page"
    
    # for main DISPLAY page
    blog_heading = models.CharField(max_length=100)
    blog_subheading = models.CharField(max_length=100)
    
    def __str__(self):
        return self.blog_heading
