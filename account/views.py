from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import RegistrationForm, LoginForm
from feed.forms import PostForm
from .models import Account, Follow
from feed.models import Post
from django import forms
from django.forms.models import model_to_dict
from django.utils.text import slugify

# Create your views here.


def index(request):

    user_name = request.session['username']
    account = get_object_or_404(Account,user_name=user_name)
    posts = Post.objects.filter(account = account) 
    followers = Follow.objects.filter(following_name= user_name)
    following = Follow.objects.filter(user_name= user_name)

    return render(request,"account/index.html",{

       "followers":followers.count(),
       "following": following.count(),
       "account":account,
       "posts": posts,
    })

def registration(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            try:
                # data = form.cleaned_data
                # print(data)
                # account = Account(first_name=data["first_name"],last_name=data["last_name"],user_name=data["user_name"],email=data["email"],profile_image=request.FILES["profile_image"],password=data["password"])
                # account.save()
                form.save()
            except:
                print("cant save!")    

            
            return HttpResponseRedirect("thank_you/")

    else:
        form = RegistrationForm()


    return render(request,"account/reg.html",{
        "form": form
    })        



def Login(request):
    error = ""
    if request.method == "POST":
        form = LoginForm(request.POST)
        
        if form.is_valid():
            try:
                data = form.cleaned_data
                print(data)
                if Account.objects.filter(user_name = data["user_name"],password = data["password"]).exists():
                    userName = data["user_name"]
                    request.session['username'] = userName
                    return HttpResponseRedirect("/")
                else:
                    error = "Wrong User Name Or Password !"
            except:
                print("cant login!")    

            
            

    else:
        form = LoginForm()


    return render(request,"account/login.html",{
        "form": form,
        "error": error
    }) 


def thank_you(request):
    if request.session.has_key('username'):
        return HttpResponseRedirect("/")

    return render(request,"account/thank_you.html")


def logout(request):
    if request.session.has_key('username'):
        del request.session['username']
    return HttpResponseRedirect("/")   

def editPost(request,slug):
    post = Post.objects.get(slug=slug)
    form = PostForm(initial=model_to_dict(post))

    if request.method == "POST":
        form = PostForm(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            post.title = data["title"]
            post.excerpt = data['excerpt']
            post.image_name = request.FILES["image"]
            post.slug = slugify(data['title'])
            post.content = data['content']
            post.save()
            for index, tag in enumerate(data['tags']):
                    post.tags.add(data['tags'][index])
    return render(request,"account/editpost.html",{
        "form":form,
    })

def updateAccount(request):
    account = get_object_or_404(Account,user_name= request.session['username'])

    if request.method == "POST":
        form = RegistrationForm(request.POST,request.FILES,instance=account)
        
        if form.is_valid():
            form.save()
            
                    


    form = RegistrationForm(initial=model_to_dict(account))
    return render(request,"account/updateaccount.html",{
        "form":form,
    })

     
