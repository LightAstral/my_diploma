from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, HostingPlan, HostingPurchase, DomainPurchase, ContactMessage


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'phone')
    readonly_fields = ('password',)


class DomainPurchaseAdmin(admin.ModelAdmin):
    list_display = ('user', 'domain_name', 'purchase_date')
    list_filter = ('user', 'purchase_date')
    search_fields = ('user__username', 'domain_name')
    date_hierarchy = 'purchase_date'


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'timestamp')
    search_fields = ('first_name', 'last_name', 'email', 'phone', 'comments')


admin.site.register(User, CustomUserAdmin)
admin.site.register(HostingPlan)
admin.site.register(HostingPurchase)
admin.site.register(DomainPurchase, DomainPurchaseAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)
