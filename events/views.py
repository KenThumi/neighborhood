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

    # if request.method == 'POST':
    #     form = ProfileForm(request.POST,request.FILES)

    #     file_to_upload = request.FILES['profile_photo']

    #     if form.is_valid():
    #         upload_result = cloudinary.uploader.upload(file_to_upload)
    #         new_result = remove_prefix(upload_result['secure_url'],'https://res.cloudinary.com/dtw9t2dom/')

    #         profile = Profile(profile_photo=new_result,
    #                           bio=form.cleaned_data['bio'],
    #                           user=request.user)

    #         profile.save_profile()

    #         messages.success(request, 'Successful profile creation.')
    #         return redirect('profile')

    ctx = {'form':form}

    return render(request,'profile/update.html',ctx)