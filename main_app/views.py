from django.shortcuts import render, redirect

# Create your views here.


def homepage(request):
    return render(request, 'homepage.html')


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

def posts(request):
    return render(request, 'posts.html')

