from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users_module.models import User

# Register your models here.

# Modufy the following code to customize user admin


admin.site.register(User, UserAdmin)
