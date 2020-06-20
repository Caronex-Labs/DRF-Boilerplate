# from allauth.account.models import EmailAddress
# from django.contrib.auth.base_user import BaseUserManager
# from django.contrib.auth.models import AbstractUser
# from django.db import models


# Create your models here.

# Uncomment and edit the following User model and the Custom UserManager to represent your needs. The following has
# been coded to use Email instead of username, feel free to modify it for any particular use-case you need it for.
# You must also uncomment a line in the settings.py file that sets this model as the Auth User Model

# class UserManager(BaseUserManager):
#     """Define a model manager for User model with no username field."""
#
#     use_in_migrations = True
#
#     def _create_user(self, email, password, **extra_fields):
#         """Create and save a User with the given email and password."""
#         if not email:
#             raise ValueError('The given email must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         if user.is_superuser:
#             EmailAddress.objects.create(user=user, email=email, primary=True, verified=True)
#
#         return user
#
#     def create_user(self, email, password=None, **extra_fields):
#         """Create and save a regular User with the given email and password."""
#         extra_fields.setdefault('is_staff', False)
#         extra_fields.setdefault('is_superuser', False)
#         return self._create_user(email, password, **extra_fields)
#
#     def create_superuser(self, email, password, **extra_fields):
#         """Create and save a SuperUser with the given email and password."""
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#
#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')
#
#         return self._create_user(email, password, **extra_fields)
#
#
# class User(AbstractUser):
#     username = None
#     user_id = models.AutoField(primary_key=True)
#     email = models.EmailField(unique=True)
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['first_name', 'last_name']
#
#     objects = UserManager()
#
#     def __str__(self):
#         return self.first_name + ' ' + self.last_name
#
#     def is_owner(self, user):
#         return self.email == user.email
