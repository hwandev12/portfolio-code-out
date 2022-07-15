from django.db import models

class AboutMe(models.Model):
    class Meta:
        verbose_name = 'About Me'
        verbose_name_plural = "About Me Page"
    
    name = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    phone = models.IntegerField(default=10)
    text = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
