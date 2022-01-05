from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
import os
from django.utils.translation import gettext_lazy
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from django.utils import timezone

# Create your models here.
class CustomAccountManager(BaseUserManager):
    def create_user(self,email,password,**other_fields):
        if not email:
            raise ValueError(gettext_lazy("You must provide an email"))
        email = self.normalize_email(email)
        user = self.model(email=email,**other_fields)

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self,email,password,**other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        return self.create_user(email,password,**other_fields)




def get_avataar_path(instance,avatar):
    pass
    return os.path.join("Avatar/{0}/{1}".format(instance.email,instance.avatar))

class NewUser(AbstractBaseUser,PermissionsMixin):
    username = None
    email = models.EmailField(gettext_lazy("email address"),unique=True) 
    name = models.CharField(max_length=200,blank = True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    start_date = models.DateField(default=timezone.now)
    avatar = models.CharField(max_length=1,null=True)
    color = models.CharField(max_length=15,null=True)
    

    objects = CustomAccountManager()


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.name+"("+self.email +")"


    

def get_file_path(instance,doc):
    pass
    instance.documentname = instance.document.name
    return os.path.join("doc/{0}/{1}".format(instance.title,instance.document))



class Post(models.Model):
    pass
    title = models.CharField(max_length=200)
    smalldescription = models.TextField(max_length=1000,null=True)
    body = RichTextUploadingField(null=True)
    publish = models.DateTimeField(auto_now_add=True)
    document = models.FileField(upload_to=get_file_path,null=True,blank=True)
    documentname = models.CharField(max_length=100,default="downloadable file")


    def __str__(self):
        return self.title

class Group(models.Model):
    groupName = models.CharField(max_length=300)

    def __str__(self):
        return self.groupName

def get_book_path(instance,book):
    instance.bookName = instance.book.name
    return os.path.join("book/{0}/{1}".format(instance.group.groupName,instance.book))

class Book(models.Model):
    title = models.CharField(max_length=300)
    group = models.ForeignKey(Group,on_delete=models.CASCADE)
    book = models.FileField(upload_to=get_book_path)
    bookName = models.CharField(max_length=300,default="downlodablefile")
    authors = models.CharField(max_length=300,blank=True,null=True)

    def __str__(self):
        return self.bookName+" ( "+self.group.groupName+" ) "

class Comment(models.Model):
    pass
    user = models.ForeignKey(NewUser,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete = models.CASCADE)
    comment = models.CharField(max_length=1000)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.name+" ( "+self.post.title +" ) "

    class Meta:
        ordering= ["time"]
    