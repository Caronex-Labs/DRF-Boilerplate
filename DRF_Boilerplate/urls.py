"""DRF_Boilerplate URL Configuration

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
from django.http import HttpResponse
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


# The following function is to be used with the password_reset_confirm URL. Scroll down for more details.
def empty_view(request):
    return HttpResponse('')


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

    # The following URL actually has no functionality. When sending an email to a user regarding their requested
    # password change, we need a url with the name 'password_reset_confirm' so that we can use it as a template to
    # create the actual URL that the user should be redirected to. This actual URL needs to point to the frontend,
    # not back to the Django backend. This pointing is done based on the 'Domain Name' you provide in the 'sites'
    # table. You can set the domain name by going to the admin panel and looking for the sites. Please refer to the
    # rest-auth documentation for more details.
    path('password-reset/<uidb64>/<token>/', empty_view, name='password_reset_confirm'),

    # Rest Auth Registration Endpoints
    path('authentication/registration/', RegisterView.as_view(), name='rest_register'),
    path('authentication/registration/verify-email/', VerifyEmailView.as_view(), name='rest_verify_email'),
    path('authentication/registration/account-confirm-email/', VerifyEmailView.as_view(),
         name='account_email_verification_sent'),
    re_path(r'^authentication/registration/account-confirm-email/(?P<key>[-:\w]+)/$', AllauthConfirmEmailView.as_view(),
            name='account_confirm_email'),

    # Documentation Endpoints
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='documentation')]
