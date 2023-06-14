from django import forms
from .models import Post, Category, Comment
from account.models import Account
from django.core.validators import *
import re

class CustomMMCF(forms.ModelMultipleChoiceField):
    def label_from_instance(self,obj):
        return obj.category

class PostForm(forms.Form):

    # class Meta:
    #     model = Post
    #     fields = ["title","excerpt","image_name","content","tags","account"]
    #     exclude = ("account",)

    
    title = forms.CharField(label="Title")
    excerpt = forms.CharField(label="Excerpt")
    image = forms.ImageField(required=False)
    content = forms.CharField(widget=forms.Textarea(attrs={'name':'content', 
                                                        }))
    # account = Account.objects.get(user_name = "shoumik").pk

    tags = CustomMMCF(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )    


class CommentForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea(attrs={'name':'comment', 
                                                        }),min_length=2)
    