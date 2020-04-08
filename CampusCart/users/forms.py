from django import forms
from django.contrib.auth.models import  User
from django.contrib.auth.forms import UserCreationForm
from  .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# a model form allows us to create aform that will work with a specific database model , in this case we want a form that will update our usermodel
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']




