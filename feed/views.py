from django.shortcuts import render
from django.contrib.comments import Comment

# Create your views here.
def comment(request, object_pk):
   mycomment = Comment.objects.get(object_pk = object_pk)
   text = '<strong>User :</strong> %s <p>'%mycomment.user_name</p>
   text += '<strong>Comment :</strong> %s <p>'%mycomment.comment</p>
   return HttpResponse(text)