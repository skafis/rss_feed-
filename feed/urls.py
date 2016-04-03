from myapp.feeds import DreamrealCommentsFeed
from django.conf.urls import patterns, url

urlpatterns += patterns('',
   url(r'^latest/comments/', DreamrealCommentsFeed()),
   url(r'^comment/(?P\w+)/', 'comment', name = 'comment'),
)