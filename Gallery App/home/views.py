from django.http.response import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from home.forms import LoginForm , SignUpForm
# Create your views here.

def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username = username, password = password)
        login(request,user)
        return HttpResponseRedirect("/")
    return render(request,"login.html",{"form":form})
def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user.save()
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})