from django.contrib import admin
from userauth.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'phone','gender')
    list_filter = ('gender', 'username','email')
    search_fields = ('email', 'username')
    list_display_links = ('id', 'username', 'email')
