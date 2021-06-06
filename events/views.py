from events.models import Profile
from events.forms import ProfileForm, UserRegisterForm
from django.shortcuts import redirect, render
from django.contrib import messages

# Create your views here.


def home(request):



    return render(request, 'index.html')


def register(request):
    form = UserRegisterForm()

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, 'Successful Registration.')

            return redirect('home')

    return render(request,'registration/register.html',{'form':form})

# @login_required
def profile(request):
    user = request.user

    return render(request,'profile/profile.html', {'user':user})


def addprof(request,id):
    form = ProfileForm()

    if request.method == 'POST':
        form = ProfileForm(request.POST)

        if form.is_valid():

            profile = Profile(
                              nat_id=form.cleaned_data['nat_id'],
                              location=form.cleaned_data['location'],
                              user=request.user)

            profile.save()

            messages.success(request, 'Successful nat. ID/neighborhood creation.')
            return redirect('profile')

    ctx = {'form':form}

    return render(request,'profile/update.html',ctx)