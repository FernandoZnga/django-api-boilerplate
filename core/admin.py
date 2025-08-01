from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Task, User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = [
        "username",
        "email",
        "first_name",
        "last_name",
        "age",
        "is_staff",
        "created_at",
    ]
    list_filter = ["is_staff", "is_superuser", "is_active", "created_at"]
    search_fields = ["username", "email", "first_name", "last_name"]
    ordering = ["-created_at"]

    fieldsets = BaseUserAdmin.fieldsets + (
        ("Additional Info", {"fields": ("age", "bio", "created_at", "updated_at")}),
    )
    readonly_fields = ["created_at", "updated_at"]


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["title", "completed", "created_by", "created_at"]
    list_filter = ["completed", "created_at", "created_by"]
    search_fields = ["title", "description"]
    ordering = ["-created_at"]
    readonly_fields = ["created_at", "updated_at"]
