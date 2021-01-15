from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


# Create your views here.

def homepage(request):
    error_message = ''
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
        else:
            error_message = "Invalid Sign Up - Please Try Again"

    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'homepage.html', context)


def logout(request):
    logout(request)
    return redirect('homepage')


@login_required(login_url='homepage')
def profile(req):
    # if req.method == 'POST':
    #     comment_form = AddComment_Form(req.POST)
    #     if comment_form .is_valid():
    #         new_comment = comment_form .save(commit=False)
    #         new_comment.user = req.user
    #         new_comment.save()
    #         return redirect('profile')
    # # Selected city
    # selected_city = City.objects.filter(id=city_id)

    # # all citys
    # cities = SelectedCity.objects.all()

    # comment_form = AddComment_Form()
    # context = {'city': selected_city, 'cities': cities}
    return render(req, 'profile.html')
