from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_organiser = models.BooleanField(default=False)
    is_agent = models.BooleanField(default=False)
    username = None
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


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

    # for detail posts
    post_text_1 = models.TextField()
    image_2 = models.ImageField(blank=True)
    post_heading_1 = models.CharField(max_length=100)
    post_text_2 = models.TextField()
    muted_text_1 = models.TextField()
    image_3 = models.ImageField(blank=True)
    post_heading_2 = models.CharField(max_length=100)
    post_text_3 = models.TextField()
    image = models.ImageField(blank=True)

    # Category
    category = models.ForeignKey(
        "Category", blank=True, null=True, on_delete=models.CASCADE)

    # for last tags
    name_blog = models.CharField(max_length=60)
    min_read = models.IntegerField(default=5)

    def __str__(self):
        return self.main_heading


# Category model for posts
class Category(models.Model):
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Category Section"

    name = models.CharField(max_length=100)
    image = models.ImageField()

    def __str__(self):
        return self.name

# contact category
class Contact_category(models.Model):
    class Meta:
        verbose_name = "Contact Category"
        verbose_name_plural = "Category Contact"

    name = models.CharField(max_length=70) 

    def __str__(self):
        return self.name



# create contact us model
class Contact(models.Model):
    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contact Us"

    TAKLIF = "TK"
    SHIKOYAT = "SK"

    CONTACT_CHOICES = [
        (TAKLIF, "Taklif"),
        (SHIKOYAT, "Shikoyat")
    ]

    your_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(max_length=600)
    category = models.ForeignKey(Contact_category, null=True, default=None, on_delete=models.CASCADE, related_name="category_contact")
    contact_choices = models.CharField(max_length=2, choices=CONTACT_CHOICES, default=TAKLIF)

    def __str__(self):
        return self.your_name
