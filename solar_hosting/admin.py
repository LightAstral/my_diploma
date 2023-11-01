# from django.contrib import admin
# from .models import User
#
#
# # Register your models here.
#
#
# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('username', 'email', 'phone')
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, HostingPlan, HostingPurchase


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'phone')
    readonly_fields = ('password',)


admin.site.register(User, CustomUserAdmin)
admin.site.register(HostingPlan)
admin.site.register(HostingPurchase)