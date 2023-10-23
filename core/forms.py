from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm ,UsernameField ,PasswordChangeForm
from django.contrib.auth.models import User
from .models import AddComplaint
from .choices import CRIME_CATEGORY



class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label="Password Again", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.CharField(required=True,widget=forms.EmailInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields=('username' ,'email')
        widgets = {'username':forms.TextInput(attrs={'class':'form-control'})}


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class' : 'form-control'}))
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete' : 'current-password' ,  'class' : 'form-control'}),
    )

class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        label="Old Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete':'current-password','autofocus':True,'class':'form-control'}),
    )
    new_password1 = forms.CharField(
        label="New Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class': 'form-control'}),
    )
    new_password2 = forms.CharField(
        label="New Password Again",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class': 'form-control'}),
    )




class AddComplaintForm(forms.ModelForm):
    class Meta:
        model = AddComplaint
        fields =("name","username","mobile_no","title","city","category","description")

        widgets ={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'username': forms.HiddenInput(attrs={'class':'form-control'}),
            'mobile_no': forms.NumberInput(attrs={'class':'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'})
        }

