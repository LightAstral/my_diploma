from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import UserCreationForm


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
            # Обработка ошибки входа
            pass
    return redirect('solar_hosting/index.html')  # Перенаправляем на главную страницу после успешного входа


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


def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'solar_hosting/dashboard.html')
    else:
        return redirect('solar_hosting:main')


def logout_view(request):
    if request.method == 'POST':
        logout(request)
    return redirect('solar_hosting:main')
