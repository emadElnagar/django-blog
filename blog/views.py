from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .form import addForm, UpdatePost,CommentForm

# Create your views here.
def blog(request):
    blog = Post.objects.all()
    paginator = Paginator(blog, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'home.html', {'posts':page_obj})


def blog_single(request, slug):
    blog_single = Post.objects.get(slug=slug)
    comment = Comment.objects.filter(post=blog_single).order_by('-id')
    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            content = request.POST.get('comment_body')
            comment = Comment.objects.create(post = blog_single, user_commented = request.user, comment_body = content)
            comment.save()
            return HttpResponseRedirect(blog_single.get_absolute_url())
    else:
        comment_form = CommentForm()
    context = {
        'post':blog_single,
        'comments':comment,
        'comment_form':comment_form
    }
    return render(request, 'blog-single.html', context)


@login_required
def add_post(request):
    if request.method=='POST':
        form = addForm(request.POST, request.FILES)
        if form.is_valid():
            myForm = form.save(commit=False)
            myForm.author = request.user
            myForm.save()
            return redirect(reverse('blog:blog_list'))

    else:
        form = addForm()
    return render(request, 'new-post.html', {'addform':form})


def update_post(request, slug):
    blog_post = get_object_or_404(Post, slug=slug)
    if request.method=='POST':
        form = UpdatePost(request.POST, request.FILES, instance=blog_post)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            blog_post = obj
            return redirect(reverse('blog:blog_list'))
    else:
        form = UpdatePost()

    form = UpdatePost(
        initial = {
            'title' : blog_post.title,
            'body' : blog_post.body,
            'image' : blog_post.image
        }
    )
    context = {
        'updateForm':form,
        'post':blog_post
    }
    return render(request, 'update-blog.html', context)


def delete_post(request, slug):
    blog_post = get_object_or_404(Post, slug=slug)
    if request.method=='POST':
        blog_post.delete()
        return redirect(reverse('blog:blog_list'))
    return render(request, 'delete-post.html', {'post':blog_post,})


@login_required
def like_post(request, slug):
    user = request.user
    if request.method == 'POST':
        post_slug = request.POST.get('post_slug')
        post_obj = Post.objects.get(slug=post_slug)
        if user in post_obj.liked.all():
            post_obj.liked.remove(user)
        else:
            post_obj.liked.add(user)
    return HttpResponseRedirect(reverse('blog:blog_single', args=[str(slug)]))