from events.models import Business, Post, Profile
from events.forms import PostForm, ProfileForm, UserRegisterForm
from django.shortcuts import redirect, render
from django.contrib import messages

# Create your views here.


def home(request):
    posts = []

    if hasattr(request.user, 'profile'):
        posts= Post.objects.filter(user__profile__location=request.user.profile.location)

    else:
        messages.warning(request, 'Kindly set your neighborhood/location and National ID.')
        return redirect('addprof')

    # print(posts.count())

    ctx = {'posts':posts}

    return render(request, 'index.html',ctx)


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


def addprof(request):
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


def getPoliceDept(request):
    dpt = Business.objects.filter(name__icontains='police',location=request.user.profile.location).first()


    ctx = {'dpt':dpt}
    

    return render(request,'dept.html',ctx)



def getHealthDept(request):
    dpt = Business.objects.filter(name__icontains='health',location=request.user.profile.location).first()


    ctx = {'dpt':dpt}
    

    return render(request,'dept.html',ctx)



def getDepts(request):
    dpts = Business.objects.filter(location=request.user.profile.location)


    ctx = {'dpts':dpts}
    

    return render(request,'depts.html',ctx)


def createPost(request):
    form = PostForm()
    
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user

            post.save()

            messages.success(request, 'Successful post creation.')
            return redirect('home')

    return render(request,'postform.html',{'form':form})
