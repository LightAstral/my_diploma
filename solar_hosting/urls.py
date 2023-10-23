from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="main"),
    path('features/', views.features, name="features"),
    path('domain/', views.domain, name="domain"),
    path('hosting/', views.hosting, name="hosting"),
    path('pricing/', views.pricing, name="pricing"),
    path('testimonials/', views.testimonials, name="testimonials"),
    path('contact/', views.contact, name="contact"),
    path('login/', views.login, name="login"),
    path('register/', views.login, name="register"),
]
