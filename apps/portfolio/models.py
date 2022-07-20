from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

# Basic home headers
class Home(models.Model):
    class Meta:
        verbose_name = 'Home'
        verbose_name_plural = "Home Page"
    
    # for main DISPLAY page
    blog_heading = models.CharField(max_length=100)
    blog_subheading = models.CharField(max_length=100)
    blog_headingImage = models.ImageField()
    
    def __str__(self):
        return self.blog_heading
    
    
# Post views
class Post(models.Model):
    class Meta:
        verbose_name = "My Post"
        verbose_name_plural = "My Posts"
        
    main_heading = models.CharField(max_length=200)
    sub_heading = models.CharField(max_length=150)
    date_post = models.CharField(max_length=100)
    
    def __str__(self):
        return self.main_heading