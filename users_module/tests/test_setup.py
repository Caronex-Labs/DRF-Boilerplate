import json
import os

from django.urls import reverse
from rest_framework.test import APITestCase

RESOURCES = os.path.join(os.path.abspath(os.path.dirname(__file__)), "resources")


class TestSetup(APITestCase):

    def setUp(self):
        self.register_url = reverse('rest_register')
        self.login_url = reverse('rest_login')

        with open(os.path.join(RESOURCES, "user_registration_data.json")) as f:
            self.user_registration_data = json.load(f)
        with open(os.path.join(RESOURCES, "user.json")) as f:
            self.user_data = json.load(f)

        return super().setUp()

    def tearDown(self):
        return super().tearDown()
