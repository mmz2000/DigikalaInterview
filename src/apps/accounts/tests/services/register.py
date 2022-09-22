import faker
from django.contrib.auth import get_user_model
from django.test import TestCase

from src.apps.accounts.functions import validate_token
from src.apps.accounts.services import register_user
from src.errors import BadRequestException, SerializerErrors


class RegisterServiceTestCase(TestCase):
    def setUp(self):
        self.faker = faker.Faker()
        self.User = get_user_model()

    def test_register_user_service(self):
        data = {
            "username": self.faker.user_name(),
            "email": self.faker.email(),
            "password": "Along@cceptabl3pAssw8rd",
            "first_name": self.faker.first_name(),
            "last_name": self.faker.last_name(),
        }
        response = register_user(data)
        self.assertEqual(response["username"], data["username"])
        self.assertEqual(response["email"], data["email"])
        self.assertEqual(response["first_name"], data["first_name"])
        self.assertEqual(response["last_name"], data["last_name"])
        self.assertIn("access_token", response)
        self.assertIn("refresh_token", response)
        self.assertTrue(validate_token(response["access_token"]))
        self.assertTrue(validate_token(response["refresh_token"]))
        self.assertNotIn("password", response)
        self.assertEqual(self.User.objects.count(), 1)
        user = self.User.objects.first()
        self.assertTrue(user.check_password(data["password"]))
        with self.assertRaises(BadRequestException) as context:
            register_user({})
        self.assertSetEqual(
            set(context.exception.error_type),
            set(SerializerErrors.create_user_serialzier.values()),
        )
        # invalid password and duplicate username
        data["password"] = "12345678"
        with self.assertRaises(BadRequestException) as context:
            register_user(data)
        self.assertSetEqual(
            set(context.exception.error_type),
            {
                SerializerErrors.create_user_serialzier.get("password"),
                SerializerErrors.create_user_serialzier.get("username"),
            },
        )
