from django.contrib import admin
from .models import MyUser
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.

class UserAdminModel(BaseUserAdmin):

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdminModel
    # that reference specific fields on auth.User.
    list_display = ["name","email","tc" ,"is_admin"]
    list_filter = ["is_admin"]
    fieldsets = [
        ("User Credentials", {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["name","tc"]}),
        ("Permissions", {"fields": ["is_admin"]}),
    ]
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdminModel
    # overrides get_fieldsets to use this attribute when creating a user.
    # if i want to add new users
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "name","tc", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["email","name"]
    ordering = ["email","id"]
    filter_horizontal = []


# Now register the new UserAdmin...
admin.site.register(MyUser, UserAdminModel)