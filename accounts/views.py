from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import login


# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login/')
        else:
            form = UserChangeForm()
            return render(request,'signup.html',{'form':form})

def thanks(request):
    return render(request,'thanks.html')