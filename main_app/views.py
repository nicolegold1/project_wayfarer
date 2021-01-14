from django.shortcuts import render, redirect

# Create your views here.


def profile(req):
    return render(req, 'profile.html')


def homepage(request):
     error_message = ''
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('wayfarer_index')
        else:
            error_message = 'Invalid sign up - try again'
    # A GET or bad POST request, renders empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'homepage.html', context)

  


   