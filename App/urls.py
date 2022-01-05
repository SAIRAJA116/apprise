from os import name
from django.urls import path
from . import views
app_name="App"

urlpatterns = [
    path("",views.index,name="index"),
    path("post/<int:id>",views.detailPost,name="detailpost"),
    path("grouplist",views.groupsList,name="grouplist"),
    path("groupbook/<int:id>",views.groupBook,name="groupbook"),
    path("logoutuser/",views.logoutuser,name="logoutuser")
]