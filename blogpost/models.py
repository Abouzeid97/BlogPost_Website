from django.db import models
from datetime import date
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.urls import reverse

# Create your models here.


class Tag(models.Model):
    caption = models.CharField(max_length=12)

    def __str__(self):
        return self.caption

class Author(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=300)
    image = models.ImageField(upload_to="author/", default="")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Post(models.Model):

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=200)
    image = models.ImageField(upload_to="post/", default="")
    content = models.TextField(validators=[MinLengthValidator(10)])
    time_posted = models.DateField()
    tag = models.ManyToManyField(Tag)
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)

    def get_absolute_url(self):
        return reverse("post-detail", args=[self.slug])

class Comment(models.Model):
    user_name= models.CharField(max_length=120)
    user_email = models.EmailField()
    text = models.TextField(max_length=600)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")