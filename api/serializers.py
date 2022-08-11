from rest_framework import serializers
from blog.models import Post, Comment
from accounts.models import Profile

# POST SERIALIZER
class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

# COMMENT SERIALIZER
class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

# PROFILE SERIALIZER
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
