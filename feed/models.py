from django.db import models
from django.core.validators import MinLengthValidator
from account.models import Account
 
# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=50)
    def __str__(self):
        return self.category


class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=150)
    image_name = models.ImageField(upload_to="post_images",null=True)
    date_time = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    account = models.ForeignKey(Account, on_delete=models.CASCADE,related_name="posts")
    tags = models.ManyToManyField(Category)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(auto_now=True)
    comment = models.CharField(max_length=1000)
    account = models.ForeignKey(Account, on_delete=models.CASCADE,related_name="comment",null=True)

    def __str__(self):
        return self.comment