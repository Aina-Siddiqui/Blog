from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegister,ProfileUpdateForm,UserUpdateForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method=='POST':
        form=UserRegister(request.POST)

        if form.is_valid():
            form.save()#this will create new user in the database
            username=form.cleaned_data.get('username')
            messages.success(request,f'Your account has been created. You can now login')
            return redirect('login')
    else:
        form=UserRegister()
    return render(request,'users/register.html',{'form':form})
@login_required
def profile(request):
    if request.method=='POST':
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpdateForm(request.POST,
                                 request.FILES,
                                 instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'your account is updated')
            return redirect('profile')
    else:
         u_form=UserUpdateForm(instance=request.user)
         p_form=ProfileUpdateForm(instance=request.user.profile)
    context={
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request,'users/profile.html',context)