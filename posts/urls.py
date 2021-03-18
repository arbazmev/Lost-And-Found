#posts url.py file

from django.conf.urls import url
from . import views

app_name ='posts'

urlpatterns = [
     url(r'^$',views.ListPost.as_view(),name='all'),
     url(r'^new/$',views.CreatePost.as_view(),name='create'),
     url(r'by/(?P<username>[-\w]+)',views.UserPosts.as_view(),name='for_user'),
     url(r'posts/in/(?P<slug>[-\w]+)/$',views.SinglePost.as_view(),name='single'),
     url(r'posts/in/(?P<slug>[-\w]+)/$',views.DeletePost.as_view(),name='delete'),
     url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='addcomment'),
     url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
]
