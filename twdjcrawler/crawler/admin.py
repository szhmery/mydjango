from django.contrib import admin
from models import Task,Proxy,Tclient
# Register your models here.

admin.site.register(Task)
admin.site.register(Proxy)
admin.site.register(Tclient)