from django.contrib import admin
from .models import *

# Register your models here.
class UserAdminConfig(admin.ModelAdmin):
    ordering=("name","email")
    list_display = ('name','email')
    search_fields = ('email','roll')

admin.site.register(NewUser,UserAdminConfig)
admin.site.register(Post)
admin.site.register(Group)
admin.site.register(Book)
admin.site.register(Comment)