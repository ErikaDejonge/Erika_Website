from django.db import models
from django.urls import reverse

# Create your models here.
class Blog(models.Model):
    blog_title = models.CharField(max_length=100)
    blog_intro = models.TextField()
    blog_body =models.TextField()
    image = models.ImageField(upload_to="Blog_media")
    # create_at = models.DateTimeField(auto_now_add=True, blank=True)
    # update_at = models.DateTimeField(auto_now=True,blank=True)

    # def __str__(self):
    #     return self.blog_title
    def get_absolute_url(self):
        return reverse("blog")

class BookErika(models.Model):
    Name = models.CharField(max_length=100)
    EventDescription = models.TextField()
    Email = models.EmailField(unique=True)
    Phone = models.CharField(max_length=10)

    def __str__(self):
        return self.Name  

class Email_Info(models.Model):
    Info_Email = models.EmailField()

    def __str__(self):
        return self.Info_Email

