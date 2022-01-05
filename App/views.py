from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import make_password, check_password
import random
# Create your views here.
def index(request):
    if request.method == "POST":
        if("login" in request.POST):
            pass
            email = request.POST.get("email")
            password = request.POST.get("password")
            user = authenticate(email=email,password = password)
            if(user is not None):
                login(request,user) 
        elif("signup" in request.POST):
            pass
            email = request.POST.get("email")
            password = request.POST.get("password")
            name = request.POST.get("name")
            print(email)
            print(email[0])
            print(email[0].upper())
            try:
                colors = ['red','Green','blue','vilot','purple','brown','orange',"#dca50a",'#b10f53',"#437807"]
                i=int(random.random()*10)
                color = colors[i]
                print(color)
                user = NewUser(email = email,name=name,password = make_password(password),color = color,avatar = email[0].upper())
                user.save()
                login(request,user)
            except:
                pass            
        return redirect("App:index")
    posts = Post.objects.all().order_by("-publish")
    return render(request,"App/index.html",{"posts":posts})

def detailPost(request,id):
    if request.method == "POST":
        if("login" in request.POST):
            pass
            email = request.POST.get("email")
            password = request.POST.get("password")
            user = authenticate(email=email,password = password)
            if(user is not None):
                login(request,user) 
        elif("signup" in request.POST):
            pass
            email = request.POST.get("email")
            password = request.POST.get("password")
            name = request.POST.get("name")
            try:
                user = NewUser(email = email,name=name,password = make_password(password))
                user.save()
                login(request,user)
            except:
                pass
        elif("cmt" in request.POST):
            try:
                comment = Comment(user=request.user,post=Post.objects.get(id=id),comment=request.POST.get("comment"))          
                comment.save()
            except:
                pass

        return redirect("App:detailpost",id)
    try:
        post = Post.objects.get(id=id)
        comments = Comment.objects.filter(post=id).order_by('-time')
        return render(request,"App/detailPost.html",{"post":post,"comments":comments})
    except:
        pass
        return redirect("App:detailpost,id")
    
def groupsList(request):
    groups = Group.objects.all()
    return render(request,"App/groupList.html",{"groups":groups})

def groupBook(request,id):
    pass
    books = Book.objects.filter(group = id)
    print(books)
    return render(request,"App/groupMaterials.html",{"books":books})

def logoutuser(request):
    pass
    logout(request)
    return redirect("App:index")