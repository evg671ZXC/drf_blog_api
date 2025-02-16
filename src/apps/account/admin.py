from django.contrib import admin

from src.apps.account.models import UserAccount
from src.apps.account.models import Profile


# Register your models here.
@admin.register(UserAccount)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_staff', 'is_superuser']


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']
    raw_id_fields = ['user', ]
