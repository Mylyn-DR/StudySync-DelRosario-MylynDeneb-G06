from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Profile, User 

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = "Profile"
    fields = ("pf_picture", "bio", "status") 

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)
    list_display = ["username", "email", "is_verified", "is_staff", "created_at"]
    list_filter = ["is_verified", "is_staff", "is_active"]

    fieldsets = UserAdmin.fieldsets + (
            ("Verification Status", {"fields": ("is_verified",)}),
        )

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "status", "updated_at"]
    search_fields = ["user__username", "user__email"]