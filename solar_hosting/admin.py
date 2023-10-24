from django.contrib import admin
from .models import User  # Импорт модели User


# Register your models here.


@admin.register(User)  # Регистрация модели User в административной панели
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone')  # Укажите поля, которые вы хотите видеть в списке
