from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import PostsSerializer, CommentsSerializer, ProfileSerializer, UserSerializer
from blog.models import Post, Comment
from accounts.models import Profile
from django.contrib.auth.models import User

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

# SINGLE COMMENT VIEW
@api_view(['DELETE', 'PUT'])
def SingleComment(request, pk):
    comment = Comment.objects.get(id=pk)
    # DELETE COMMENT
    if request.method == 'DELETE':
        if comment:
            comment.delete()
            return Response({"status":"ok"}, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    # UPDATE COMMENT
    elif request.method == 'PUT':
        if comment:
            serializer = CommentsSerializer(comment, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# CREATE A NEW POST
@api_view(['POST'])
def CreateNewPost(request):
    serializer = PostsSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# DELETE POST
@api_view(['DELETE'])
def DeletePost(request, slug):
    post = Post.objects.get(slug = slug)
    if post:
        post.delete()
        return Response({"status":"ok"}, status = status.HTTP_200_OK)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# UPDATE POST
@api_view(['PUT'])
def UpdatePost(request, slug):
    post = Post.objects.get(slug = slug)
    if post:
        serializer = PostsSerializer(post, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# ==================== USERS API ==================== #

# GET USER PROFILE
@api_view(['GET'])
def UserProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    serializer = ProfileSerializer(profile, many = False)
    return Response(serializer.data)

# UPDATE PROFILE
@api_view(['PUT'])
def UpdateProfile(request):
    profile = Profile.objects.get(user=request.user)
    serializer = ProfileSerializer(profile, data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# USER SIGNUP
@api_view(['POST'])
def SignUp(request):
    serializer = UserSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# UPDATE USER DATA
@api_view(['PUT'])
def UserUpdate(request):
    user = request.user
    serializer = UserSerializer(user, data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# DELETE USER ACCOUNT
@api_view(['DELETE'])
def DeleteUser(request, pk):
    user = User.objects.get(pk=pk)
    if user:
        user.delete()
        return Response({"status":"ok"}, status = status.HTTP_200_OK)
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
