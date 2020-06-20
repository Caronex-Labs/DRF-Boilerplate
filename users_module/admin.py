# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.utils.translation import ugettext_lazy as _
#
# from users_module.models import User

# Register your models here.

# Uncomment the following lines to register the custom user model on the Django Admin Panel.

# @admin.register(User)
# class UserAdmin(BaseUserAdmin):
#     """Define admin model for custom User model with no email field."""
#
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         (_('Personal info'), {'fields': ('first_name', 'last_name')}),
#         (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
#                                        'groups', 'user_permissions')}),
#         (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'password1', 'password2', 'first_name', 'last_name'),
#         }),
#     )
#     list_filter = ('groups',)
#     list_display = ('email', 'first_name', 'last_name')
#     search_fields = ('email', 'first_name', 'last_name')
#     ordering = ('email',)
