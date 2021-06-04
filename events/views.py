from events.forms import UserRegisterForm
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



