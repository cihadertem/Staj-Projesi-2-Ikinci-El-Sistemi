from django.contrib import admin
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm

    fieldsets = [
        *UserAdmin.fieldsets,
        (
            'Kullanıcı Bilgileri',
            {
                'fields': (
                    'gender',
                    'bio',
                    'avatar',
                    'birthdate',
                )
            }

        )
    ]
admin.site.register(CustomUser, CustomUserAdmin)
