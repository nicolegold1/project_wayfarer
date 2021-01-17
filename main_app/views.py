from django.contrib.auth.models import User
from django.db.models import signals
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import City, Profile, Post
from .forms import Post_Form, City_Form

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


def profile(req):
    # user = User.objects.get(user_id=req.user_id)
    # user.save()
    if req.method == 'POST':
        form = Post_Form(req.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = req.user.profile
            new_post.save()
            return redirect('profile')
    # posts The users post
    posts = Post.objects.filter(user=req.user.profile)
    # all citys
    cities = City.objects.filter(user=req.user)
    # profile
    profile = Profile.objects.get(user=req.user)
    post_form = Post_Form()
    context = {'cities': cities, 'posts': posts,
               'post_form': post_form, 'profile': profile}
    return render(req, 'profile.html', context)
    # Selected city
    # selected_city = City.objects.filter(id=city_id)

    # 'city': selected_city,
    # comment_form = AddComment_Form()


def post(req, post_id):
    post = Post.objects.get(id=post_id)
    # if request.method == "POST":
    #     title = request.POST['title']
    #     content = request.POST['content']
    #     username_form = request.POST['username']
    context = {'post': post}
    return render(req, 'post.html', context)


""" def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
    return redirect('profile') """


def posts_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {'post': post}
    return render(request, 'post.html', context)


def city(req):
    # create
    if req.method == 'POST':
        city_form = City_Form(req.POST)
        if city_form.is_valid():
            new_city = city_form.save(commit=False)
            new_city.user = req.user
            new_city.save()
            return redirect('city_index')
    city_form = City_Form()
    context = {'city': city, 'city_form': city_form}
    return render(req, 'cities/index.html', context)


def city_detail(req, city_id):
    # create
    if req.method == 'POST':
        city_form = City_Form(req.POST)
        if city_form.is_valid():
            new_city = city_form.save(commit=False)
            new_city.user = req.user
            new_city.save()
            return redirect('city_index')

    city = City.objects.get(id=city_id)
    city_form = City_Form()
    context = {'city': city, 'city_form': city_form}
    return render(req, 'cities/detail.html', context)


@login_required
def city_edit(req, city_id):
    city = City.objects.get(id=city_id)
    if req.method == 'POST':
        city_form = City_Form(req.POST, instance=city)
        if city_form.is_valid():
            city_form.save()
            return redirect('city_detail', city_id=city.id)

    city_form = City_Form(instance=city)
    context = {'city_form': city_form, 'city': city}
    return render(req, 'cities/edit.html', context)
