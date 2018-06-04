from django.shortcuts import render_to_response

from blog.models import Author, Book
from django import forms
from django.http import HttpResponse

class UserForm(forms.Form):
    name = forms.CharField()


class UserForm2(forms.Form):
    username = forms.CharField()
    headImg = forms.FileField()


# Create your views here.
def show_author(req):
    authors = Author.objects.all()
    return render_to_response('show_author.html', {'authors': authors})


def show_book(req):
    books = Book.objects.all()
    return render_to_response('show_book.html', {'books': books})


def register(req):
    if req.method == 'POST':
        form = UserForm(req.POST)  #binding
        if form.is_valid():
            print form.cleaned_data  #get form data
            return HttpResponse('ok')
    else:
        form = UserForm()
    return render_to_response('register.html',{'form':form})

def regist(req):
    if req.method == 'POST':
        uf = UserForm2(req.POST, req.FILES)
        if uf.is_valid():
            print uf.cleaned_data['username']
            print uf.cleaned_data['headImg'].name
            print uf.cleaned_data['headImg'].size
            fp = file('/upload/'+ uf.cleaned_data['headImg'].name,'wb')
            s = uf.cleaned_data['headImg'].read()
            fp.write(s)
            fp.close()
            return HttpResponse('ok')
    else:
        uf = UserForm2()
    return render_to_response('regist.html',{'uf':uf})