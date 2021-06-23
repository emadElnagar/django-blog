from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls.base import reverse
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .forms import SignupForm , UserForm, ProfileForm
from .models import Profile
from blog.models import Post


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form':form})


def profile(request, id):
    profile = Profile.objects.get(id=id)
    user_posts = Post.objects.filter(author=profile.user).order_by('-last_update')
    return render(request, 'profile/profile.html', {'profile':profile, 'posts':user_posts})


def profile_edit(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        userform = UserForm(request.POST, instance=request.user)
        profileform = ProfileForm(request.POST, request.FILES, instance=profile)
        if userform.is_valid() and profileform .is_valid():
            userform.save()
            myProfile = profileform.save(commit=False)
            myProfile.user = request.user
            myProfile.save()
            return redirect(reverse('accounts:profile', kwargs={"id": profile.id}))
    else:
        userform = UserForm(instance=request.user)
        profileform = ProfileForm(instance=profile)
    return render(request, 'profile/profile-edit.html', {
        'userform':userform,
        'profileform':profileform,
    })


def change_password(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect(reverse('accounts:profile', kwargs={"id": profile.id}))
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/password_change_form.html', {'form': form, 'profile': profile})