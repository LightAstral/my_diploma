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
    list_filter = ('read',)
    actions = ['mark_as_read', 'mark_as_unread']

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['unread_count'] = ContactMessage.objects.filter(read=False).count()
        return super(ContactMessageAdmin, self).changelist_view(request, extra_context=extra_context)

    def mark_as_read(self, request, queryset):
        queryset.update(read=True)

    mark_as_read.short_description = "Mark selected messages as read"

    def mark_as_unread(self, request, queryset):
        queryset.update(read=False)

    mark_as_unread.short_description = "Mark selected messages as unread"


admin.site.register(User, CustomUserAdmin)
admin.site.register(HostingPlan)
admin.site.register(HostingPurchase)
admin.site.register(DomainPurchase, DomainPurchaseAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)


admin.site.index_template = 'admin/base_site.html'
