from django  import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegister(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=['username','email','password1','password2']
#ModelForm allows us to create a form that will work specific databse model
#In this case we want a form that will update user model
class UserUpdateForm(forms.ModelForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=['username','email']
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['image']
