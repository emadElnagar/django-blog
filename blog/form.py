from django import forms
from .models import Post, Comment

class addForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ('author','slug','liked')


class UpdatePost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'image']
    
    def save(self, commit=True):
        blog_post = self.instance
        blog_post.title = self.cleaned_data['title']
        blog_post.body = self.cleaned_data['body']

        if self.cleaned_data['image']:
            blog_post.image = self.cleaned_data['image']
        
        if commit:
            blog_post.save()
        return blog_post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_body']
    comment_body = forms.CharField(label ="", widget = forms.Textarea(
    attrs ={
        'placeholder':'Write your comment here ...',
    }))