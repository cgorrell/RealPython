from django.conf.urls import patterns, include, url
from blog import views

urlpatterns = patterns('',
	url(r'^$', views.index, name ='index'),
	url(r'^add_posts/$', views.add_posts, name = 'add_posts'),
	url(r'^(?P<post_name>\w+)/$', views.post, name='post'),
)