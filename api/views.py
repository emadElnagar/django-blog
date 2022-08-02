from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostsSerializer
from blog.models import Post, Comment

# GET ALL POSTS
@api_view(['GET'])
def PostsList(request):
    posts = Post.objects.all()
    serializer = PostsSerializer(posts, many = True)
    return Response(serializer.data)

# GET SINGLE POST
@api_view(['GET'])
def SinglePost(request, slug):
    post = Post.objects.get(slug=slug)
    serializer = PostsSerializer(post, many = False)
    return Response(serializer.data)
