from django.shortcuts import render, redirect
from . forms import RegisterForm, changeUserData
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

# Create your views here.

def home(request):
    return render(request, './home.html')

def signup(request):
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Account created successfully')
            form.save()
            print(form.cleaned_data)
    else:
        form = RegisterForm()
    return render(request, './signup.html', {'form': form})

def user_login(request):
    if request.user.is_authenticated:
        return redirect('profile')
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data = request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username = name, password = user_pass)
            if user is not None:
                login(request, user)
                return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
    
def profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        form = changeUserData(request.POST, instance = request.user)
        if form.is_valid():
            messages.success(request, 'Account updated successfully')
            form.save()
            print(form.cleaned_data)
    else:
        form = changeUserData(instance = request.user)
    return render(request, './profile.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

def pass_change(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        form = PasswordChangeForm(user = request.user, data = request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, './passchange.html', {'form': form})

def pass_change2(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        form = SetPasswordForm(user = request.user, data = request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('profile')
    else:
        form = SetPasswordForm(user=request.user)
    return render(request, './passchange.html', {'form': form})

def change_user_data(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        form = changeUserData(request.POST)
        if form.is_valid():
            messages.success(request, 'Account updated successfully')
            form.save()
            print(form.cleaned_data)
    else:
        form = changeUserData()
    return render(request, './profile.html', {'form': form})