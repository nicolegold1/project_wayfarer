from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import City, Profile, Post
from .forms import Post_Form

# Create your views here.


def homepage(request):
    error_message = ''
    if request.method == "POST":
        if request.POST.get('submit') == 'sign_up':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('profile')
            else:
                error_message = "Invalid Sign Up - Please Try Again"
        elif request.POST.get('submit') == 'sign_in':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
            else:
                error_message = "Invalid Sign In Credentials - Please Try Again"
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'homepage.html', context)


def logout(request):
    logout(request)
    return redirect('homepage')


@login_required(login_url='homepage')
def profile(req):
    if req.method == 'POST':
        form = Post_Form(req.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = req.user
            new_post.save()
            return redirect('profile')
    # all citys
    cities = City.objects.all()
    # posts
    posts = Post.objects.all()
    # profile
    profile = Profile.objects.all()
    post_form = Post_Form()
    context = {'cities': cities, 'posts': posts,
               'post_form': post_form, 'profile': profile}
    return render(req, 'profile.html', context)
    # Selected city
    # selected_city = City.objects.filter(id=city_id)


# 'city': selected_city,
    # comment_form = AddComment_Form()


# def post(request):
#     if request.method == "POST":
#         title = request.POST['title']
#         content = request.POST['content']
#         username_form = request.POST['username']
#     return redirect('posts')


# def post_create(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save()
#             return redirect('profile')
