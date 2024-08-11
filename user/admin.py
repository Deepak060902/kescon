from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import KesconUser, Address
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = KesconUser
    list_display = ['username', 'e_mail', 'first_name', 'last_name', 'is_staff', 'is_active']
    list_filter = ['is_staff', 'is_active']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'phone_number', 'e_mail', 'city', 'state', 'postal_code', 'country')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'e_mail', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('username', 'e_mail')
    ordering = ('username',)

admin.site.register(KesconUser, CustomUserAdmin)
admin.site.register(Address)
