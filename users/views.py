from django.shortcuts import render, redirect, Http404
from .forms import LoginForm, RegisterForm, ProfileUpdateForm
from django.contrib.auth import authenticate, login, logout

def editprofile_view(request):
    form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('users:profile')

    return render(request, "users/form.html", {"form": form, 'title': 'Profili Düzenle'})
    def get_object(self):
        return self.request.user

def profile_view(request):
    if not request.user.is_authenticated:
        raise Http404()
    return render(request, 'users/profile.html')

def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home')
    return render(request, "users/form.html", {"form": form, 'title': 'Giriş Yap'})

def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password1')
        user.set_password(password)
        # user.is_staff = user.is_superuser = True
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return redirect('home')

    return render(request, "users/form.html", {"form": form, 'title': 'Üye Ol'})

def logout_view(request):
    if not request.user.is_authenticated:
        raise Http404()
    logout(request)
    return redirect('home')