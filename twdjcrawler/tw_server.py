from twisted.internet import reactor
from twisted.internet.protocol import Factory,Protocol

import sys
import os
import time
sys.path.insert(0,r"/home/odl/zhaohsun/python/django-project/twdjcrawler")

from django.conf import  settings

os.environ['DJANGO_SETTINGS_MODULE']='twdjcrawler.settings'

from django.db.models.loading import get_models
loaded_models = get_models()

from crawler.models import Task
tasks=[]

def get_tasks():
        #while True:
        time.sleep(5)
        tks = Task.objects.filter(status=0)
        tasks.extend(tks)
        print tasks
class SendTask(Protocol):
    def connectionMade(self):
        tobj = tasks.pop()
        self.transport.write(str(tobj.url))
        tobj.status = 1
        tobj.save()
        #self.transport.loseConnection()

    def dataReceived(self, data):
        print data
        #self.transport.write("haha:"+data)

factory = Factory()
factory.protocol = SendTask

reactor.callLater(1,get_tasks)
reactor.listenTCP(8001,factory)
reactor.run()