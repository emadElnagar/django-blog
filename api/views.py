from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import PostsSerializer, CommentsSerializer
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

# POST COMMENTS VIEW
@api_view(['GET', 'POST'])
def PostComments(request, slug):
    # GET COMMENTS OF POST
    post = Post.objects.get(slug=slug)
    if request.method == 'GET':
        comments = Comment.objects.filter(post = post)
        serializer = CommentsSerializer(comments, many = True)
        return Response(serializer.data)
    # CREATE A NEW COMMENT
    elif request.method == 'POST':
        serializer = CommentsSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# CREATE A NEW POST
@api_view(['POST'])
def CreateNewPost(request):
    serializer = PostsSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
