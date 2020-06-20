"""DRF_Rest_Auth_Boilerplate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# All Auth
from allauth.account.views import ConfirmEmailView as AllauthConfirmEmailView
# Django Imports
from django.contrib import admin
from django.urls import path, re_path
# Auto Documentation
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
# Rest Auth
from rest_auth.registration.views import VerifyEmailView, RegisterView
from rest_auth.views import (
    LoginView, PasswordChangeView, PasswordResetView, PasswordResetConfirmView, LogoutView
)
# Rest Framework
from rest_framework import permissions

# Setup for Swagger Documentation
schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Inbuilt Endpoints
    path('admin/', admin.site.urls),

    # Rest Auth Endpoints
    path('authentication/password/reset/', PasswordResetView.as_view(), name='rest_password_reset'),
    path('authentication/password/reset/confirm/', PasswordResetConfirmView.as_view(),
         name='rest_password_reset_confirm'),
    path('authentication/login/', LoginView.as_view(), name='rest_login'),
    path('authentication/logout/', LogoutView.as_view(), name='rest_logout'),
    path('authentication/password/change/', PasswordChangeView.as_view(), name='rest_password_change'),

    # Rest Auth Registration Endpoints
    path('authentication/registration/', RegisterView.as_view(), name='rest_register'),
    path('authentication/registration/verify-email/', VerifyEmailView.as_view(), name='rest_verify_email'),
    path('authentication/registration/account-confirm-email/', VerifyEmailView.as_view(),
         name='account_email_verification_sent'),
    re_path(r'^authentication/registration/account-confirm-email/(?P<key>[-:\w]+)/$', AllauthConfirmEmailView.as_view(),
            name='account_confirm_email'),

    # Documentation Endpoints
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='documentation')]
