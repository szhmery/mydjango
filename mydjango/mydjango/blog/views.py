from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,Context
from django.shortcuts import render_to_response
# Create your views here.

# def index(req):
#     t = loader.get_template("index.html")
#     c = Context({})
#
#     return HttpResponse(t.render(c))

def index(req):
    return render_to_response('index.html',{})