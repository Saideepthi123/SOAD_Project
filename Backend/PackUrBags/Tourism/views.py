from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from Tourism.forms import RegistrationForm, AccountAuthenticationForm


def homepage(request):
    return render(request, 'homepage.html', {})


def registration_view(request):
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('home')
    else:
        form = RegistrationForm()
        return render(request, 'user_register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/')


def login_view(request):
    user = request.user
    if user.is_authenticated:
        return redirect("home")

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("home")

    else:
        form = AccountAuthenticationForm()

    return render(request, "user_login.html", {'login_form': form})
