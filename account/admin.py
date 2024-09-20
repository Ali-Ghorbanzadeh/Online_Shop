from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'balance', 'is_banned')
    search_fields = ['user']
    list_filter = ['is_banned']