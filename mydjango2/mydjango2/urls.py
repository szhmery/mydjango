from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mydjango2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$','blog2.views.index'),
    url(r'^index1/$','blog2.views.index1'),
    url(r'^index2/$', 'blog2.views.index2')

)
