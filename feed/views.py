from django.shortcuts import render, get_object_or_404
from .forms import PostForm, CommentForm
from .models import Post,Comment
from account.models import Account
from django.utils.text import slugify
from django.http import HttpResponseRedirect


# Create your views here.

def index(request):

    if request.session.has_key('username'):
        username = request.session['username']

        posts = Post.objects.all()
        return render(request,"feed/index.html",{
            "username":username,
            "posts":posts
        })
    
    else:
        return HttpResponseRedirect("account/login/")

def add_post(request):
    if request.session.has_key('username'):
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                account = Account.objects.get(user_name = request.session['username'])
                post = Post(title = data['title'],excerpt=data['excerpt'],image_name=request.FILES["image"]
                        ,content=data['content'],account=account,slug = slugify(data['title']))
                post.save()
                print(post)
                for index, tag in enumerate(data['tags']):
                    post.tags.add(data['tags'][index])
                
            
            

        else:
            form = PostForm()

        return render(request,"feed/createPost.html",{
            "form": form
        })     
    
    else:
        return HttpResponseRedirect("/")
    


def post_detail(request, slug):
    post = get_object_or_404(Post,slug = slug)
    comments = Comment.objects.filter( post = post)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            account = Account.objects.get(user_name = request.session['username'])
            comment = Comment(post=post,comment=data['comment'],account=account)
            comment.save()
    else:
        form = CommentForm()
    
    
    
    return render(request,"feed/postDetail.html",{
        "post": post,
        "tags": post.tags.all,
        "form": form,
        "comments": comments
    })


def explore(request):

    posts = Post.objects.all()
    return render(request,"feed/explore.html",{
        
        "posts":posts
    })

    