from django.conf.urls import patterns, include, url

from django.contrib import admin
#from blog.views import index
admin.autodiscover()

urlpatterns = patterns('blog.views',
    # Examples:
    # url(r'^$', 'mydjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    #url(r'^blog/index/$','blog.views.index'),
    #url(r'^blog/index/$', index),
    url(r'^blog/index/(\d{2})/$', 'index'),
)
