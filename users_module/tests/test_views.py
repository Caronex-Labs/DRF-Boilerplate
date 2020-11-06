import pdb
from allauth.account.models import EmailAddress

from rest_framework import status

from users_module.tests.test_setup import TestSetup


class TestViews(TestSetup):
    def test_user_registration_success(self):
        res = self.client.post(
            self.register_url, self.user_registration_data, format="json"
        )
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_user_registration_failure_no_data(self):
        res = self.client.post(self.register_url)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_login_failure_unverified(self):
        self.client.post(self.register_url, self.user_registration_data, format="json")
        res = self.client.post(self.login_url, self.user_data, format="json")
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_login_success(self):
        self.client.post(
            self.register_url, self.user_registration_data, format="json"
        )
        print(self.user_registration_data)
        email = self.user_registration_data["email"]
        user = EmailAddress.objects.get(email=email)
        user.verified = True
        user.save()
        res = self.client.post(self.login_url, self.user_data, format="json")
        print(res.json())
        self.assertEqual(res.status_code, status.HTTP_200_OK)
