from django.db import models

# Create your models here.


class Account(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100,db_index=True)
    email = models.EmailField()
    profile_image = models.ImageField( upload_to="profiles", null=True)
    password = models.CharField(max_length=100)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


class Follow(models.Model):
    user_name = models.CharField(max_length=100)
    following_name = models.CharField(max_length=100)