from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from apps.user.models import Insurer, AssessorExpert, Admin


class InsurerInline(admin.StackedInline):
    model = Insurer
    can_delete = False


class AssessorExpertInline(admin.StackedInline):
    model = AssessorExpert
    can_delete = False


class AdminInline(admin.StackedInline):
    model = Admin
    can_delete = False


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (InsurerInline,AssessorExpertInline,AdminInline)


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
