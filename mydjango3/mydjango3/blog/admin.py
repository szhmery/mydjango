from django.contrib import admin

# Register your models here.
from blog.models import User
from blog.models import FileUser
admin.site.register(User)
admin.site.register(FileUser)
