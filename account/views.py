from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import RegistrationForm, LoginForm
from .models import Account
from feed.models import Post
from django import forms

# Create your views here.


def index(request):
    return render(request,"account/index.html")

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


def profile(request,slug):
    profile = get_object_or_404(Account,user_name = slug)
    posts = Post.objects.filter(account=profile)
    print(posts)
    return render(request,"account/profile.html",{
        "profile":profile,
        "posts" : posts
    })
     
