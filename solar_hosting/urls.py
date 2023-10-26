from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'solar_hosting'

urlpatterns = [
    path('', views.index, name="main"),
    path('features/', views.features, name="features"),
    path('domain/', views.domain, name="domain"),
    path('hosting/', views.hosting, name="hosting"),
    path('pricing/', views.pricing, name="pricing"),
    path('testimonials/', views.testimonials, name="testimonials"),
    path('contact/', views.contact, name="contact"),
    path('login/', views.login_view, name="login"),
    path('registration/', views.registration_view, name="registration"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('profile/', views.profile, name='profile'),
    path('settings/', views.settings, name='settings'),
    path('change_settings/', views.change_settings, name='change_settings'),
    path('logout/', views.logout_view, name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)