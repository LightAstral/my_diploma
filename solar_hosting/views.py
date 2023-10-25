from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'solar_hosting/index.html')


def features(request):
    return render(request, 'solar_hosting/features.html')


def domain(request):
    return render(request, 'solar_hosting/domain.html')


def hosting(request):
    return render(request, 'solar_hosting/hosting.html')


def pricing(request):
    return render(request, 'solar_hosting/pricing.html')


def testimonials(request):
    return render(request, 'solar_hosting/testimonials.html')


def contact(request):
    return render(request, 'solar_hosting/contact.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('solar_hosting:dashboard')
        else:
            messages.error(request, 'Неправильное имя пользователя или пароль. Попробуйте ещё раз.')
            # Вы можете добавить другую обработку ошибки, если необходимо
    return redirect('solar_hosting:main')  # Перенаправляем на главную страницу после неудачного входа


def registration_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('solar_hosting:dashboard')  # Перенаправляем на главную страницу после успешной регистрации
    else:
        form = UserCreationForm()
    return render(request, 'solar_hosting/index.html', {'form': form})


@login_required
def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'solar_hosting/dashboard.html')
    else:
        return redirect('solar_hosting:main')


@login_required
def profile(request):
    # Логика для отображения профиля пользователя
    return render(request, 'solar_hosting/profile.html')


@login_required
def settings(request):
    # Логика для отображения настроек пользователя
    return render(request, 'solar_hosting/settings.html')


def logout_view(request):
    if request.method == 'POST':
        logout(request)
    return redirect('solar_hosting:main')
