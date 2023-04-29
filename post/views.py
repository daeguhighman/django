from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from .models import Post

##from django.http import JsonResponse

from rest_framework.decorators import api_view

from .serializers import PostSerializer

@api_view(['POST'])
def CreatePostView(request):
  title = request.data.get('title')
  content = request.data.get('content')
  post = Post.objects.create(title=title, content=content)
  return Response({"msg":f"'{post.title}'이 생성되었어요!"})

# 아래에 추가해주세요! 

@api_view(['GET'])
def ReadAllPostView(request):
    posts = Post.objects.all()
    contents = [{post.title:post.content} for post in posts]
    ##return JsonResponse({"posts":contents})
    return Response({"posts":contents})
  
from django.urls import path
from .views import ReadAllPostView, CreatePostView

app_name = 'post'
urlpatterns = [
    # FBV url path
    path("register_post/", CreatePostView, name='post'),
    path("see_post/", ReadAllPostView, name="get")
]

...
from rest_framework.views import APIView
from rest_framework import status
...

class PostListView(APIView):

		### 얘네가 class inner function 들! ###
    def get(self, request): 
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        

    def post(self, request):
        title = request.data.get('title')
        content = request.data.get('content')
        if not title or not content:
            return Response({"detail": "[title, content] fields missing."}, status=status.HTTP_400_BAD_REQUEST)
        post = Post.objects.create(title=title, content=content)

        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
class PostDetailView(APIView):
    def get(self, request, post_id):
        try:
            post = Post.objects.get(id=post_id)
        except:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    def delete(self, request, post_id):
        try:
            post = Post.objects.get(id=post_id)
        except:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)