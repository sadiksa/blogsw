from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

# Create your models here.


class Category(models.Model):
	name = models.CharField(max_length=25)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("home")

class Post(models.Model):
    title = models.CharField(max_length=25, default="Post Title")
    header_image = models.ImageField(null=False, blank=False, default="images/default_image.jpg", upload_to="images/")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # body = models.TextField()
    body = RichTextField(blank=True, null=True)
    post_date = models.DateTimeField(auto_now_add=True)
    # image_link = models.CharField(max_length=255, default="/images/default_image.jpg")
    category = models.CharField(max_length=25, default="Uncategorized")
    likes = models.ManyToManyField(User, related_name="blog_posts")

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse("postdetail", args=[str(self.id)])
