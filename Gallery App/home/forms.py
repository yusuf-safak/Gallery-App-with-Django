from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.forms.forms import Form
from django.forms.widgets import PasswordInput
from django.contrib.auth.forms import UserCreationForm
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100,label="Kullanıcı Adı")
    password = forms.CharField(max_length=15,label="Parola", widget=forms.PasswordInput)
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user  = authenticate(username = username, password = password)
            if not user:
                raise forms.ValidationError("Kullanıcı adı veya parola yanlış..!")
        return super(LoginForm,self).clean()
class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=False)
    password1 = forms.CharField(max_length=30, required=False,widget=forms.PasswordInput) 
    password2 = forms.CharField(max_length=30, required=False, widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = [
            "username",
            "password1",
            "password2",
        ]
