from django.contrib import admin
from userauth.models import User, Profile
from django.utils.html import format_html


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "phone", "gender")
    list_filter = ("gender", "username", "email")
    search_fields = ("email", "username")
    list_display_links = ("id", "username", "email")


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["fullname", "gender", "relationship", "date", "display_image"]
    list_display_links = ("fullname", "gender", "relationship", "date", "display_image")

    def display_image(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width: 50px; height: 50px;" />', obj.image.url
            )
        else:
            return "No Cover"
