# from rest_auth.registration.serializers import RegisterSerializer
# from rest_auth.serializers import LoginSerializer
# from rest_framework import serializers


# Uncomment the following serializers to set up custom serializers for login and registration. You will also have to
# uncomment lines in the settings.py file in order to use custom serializers.

#
# class CustomLoginSerializer(LoginSerializer):
#     username = None
#     email = serializers.EmailField(required=True)
#     password = serializers.CharField(style={'input_type': 'password'})
#
#
# class CustomRegisterSerializer(RegisterSerializer):
#     username = None
#     first_name = serializers.CharField(max_length=100)
#     last_name = serializers.CharField(max_length=100)
#     # custom_field = serializers.CharField(max_length=100)

#
#     # def validate_custom_field(self, custom_field):
#     #     if custom_field in User.objects.all().values_list('custom_field', flat=True):
#     #         raise serializers.ValidationError("A user with that custom_field already exists.")
#     #     return custom_field
#
#     def get_cleaned_data(self):
#         return {
#             'password1': self.validated_data.get('password1', ''),
#             'email': self.validated_data.get('email', ''),
#             'first_name': self.validated_data.get('first_name', ''),
#             'last_name': self.validated_data.get('last_name', ''),
#             # 'custom_field': self.validated_data.get('custom_field', ''),
#         }
#
#     # def custom_signup(self, request, user):
#         # user.custom_field = self.get_cleaned_data().get("custom_field")
#         # user.save()
