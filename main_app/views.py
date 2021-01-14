from django.shortcuts import render, redirect

# Create your views here.


def profile(req):
    return render(req, 'profile.html')


def homepage(request):
    return render(request, 'homepage.html')

def posts(request):
    return render(request, 'posts.html')
