from django.contrib import admin
from .models import NewUser
from django.db import models
from django.forms import Textarea


# Register your models here.

class UserModelAdmin(admin.ModelAdmin):
    model = NewUser
    search_fields = ('email', 'user_name', 'first_name',)
    list_filter = ('email', 'user_name', 'first_name', 'is_active', 'is_staff')
    ordering = ('-created_at',)
    list_display = ('email', 'user_name', 'last_name', 'date_of_birth',
                    'is_active', 'is_staff', 'change_button', 'delete_button')
    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'first_name', 'last_name', 'date_of_birth', 'photo')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 20, 'cols': 60})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'first_name', 'password1', 'password2', 'is_active', 'is_staff',)}
         ),
    )


admin.site.register(NewUser, UserModelAdmin)
