from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from .forms import CustomUserCreationForm, UserProfileForm, EmailChangeForm, PhoneChangeForm
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
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
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('solar_hosting:dashboard')  # Перенаправляем на главную страницу после успешной регистрации
    else:
        form = CustomUserCreationForm()
    return render(request, 'solar_hosting/index.html', {'form': form})


@login_required
def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'solar_hosting/dashboard.html')
    else:
        return redirect('solar_hosting:main')


@login_required
def profile(request):
    user = request.user
    return render(request, 'solar_hosting/profile.html', {'user': user})


@login_required
def settings(request):
    # Логика для отображения настроек пользователя
    return render(request, 'solar_hosting/settings.html')


def logout_view(request):
    if request.method == 'POST':
        logout(request)
    return redirect('solar_hosting:main')


@login_required
def change_settings(request):
    profile_form = CustomUserCreationForm(instance=request.user)
    email_form = EmailChangeForm(initial={'email': request.user.email})
    phone_form = PhoneChangeForm(initial={'phone': request.user.phone})
    password_form = PasswordChangeForm(request.user)

    if request.method == 'POST':
        action = request.GET.get('action')
        if action == 'profile':
            profile_form = CustomUserCreationForm(request.POST, instance=request.user)
            if profile_form.is_valid():
                profile_form.save()
                messages.success(request, 'Личные данные обновлены успешно.')

        elif action == 'email':
            email_form = EmailChangeForm(request.POST)
            if email_form.is_valid():
                new_email = email_form.cleaned_data['email']
                request.user.email = new_email
                request.user.save()
                messages.success(request, 'Email успешно изменен.')

        elif action == 'phone':
            phone_form = PhoneChangeForm(request.POST)
            if phone_form.is_valid():
                new_phone = phone_form.cleaned_data['phone']
                request.user.phone = new_phone
                request.user.save()
                messages.success(request, 'Телефон успешно изменен.')

        elif action == 'password':
            password_form = PasswordChangeForm(request.user, request.POST)
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)  # Обновляет сессию после смены пароля
                messages.success(request, 'Пароль успешно изменен.')

    return render(request, 'solar_hosting/settings.html', {
        'profile_form': profile_form,
        'email_form': email_form,
        'phone_form': phone_form,
        'password_form': password_form,
    })