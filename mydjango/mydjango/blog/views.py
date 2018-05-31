from django.shortcuts import render_to_response


# Create your views here.

# def index(req):
#     t = loader.get_template("index.html")
#     c = Context({})
#
#     return HttpResponse(t.render(c))
class Person(object):
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def say(self):
        return "I am "+self.name


def index(req, parm):
    user = {'name':'tom','age':23,'sex':'female'}
    #user = Person('Tom', 23, 'male')
    book_list = ['python', 'java', 'php', 'web']
    return render_to_response('index.html', {'title': 'my page',  'book_list': book_list,'user': user, 'id':parm})
