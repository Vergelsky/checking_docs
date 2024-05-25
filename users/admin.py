from django.contrib import admin

from users.models import User


# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_moderator', 'is_staff', 'is_superuser')

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if not change:
            obj.set_password(obj.password)
        if obj.is_moderator:
            obj.is_staff = True
        else:
            obj.is_staff = False
            obj.user_permissions.clear()
        obj.save()
