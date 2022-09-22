from django.test import TestCase

from src.utils import validate_password


class ValidatePasswordUtilTestCase(TestCase):
    def test_validate_password(self):
        # Test password with less than 8 characters
        self.assertFalse(validate_password("1234567"))
        # Test password with no alphabet
        self.assertFalse(validate_password("12345678"))
        # Test password with no uppercase
        self.assertFalse(validate_password("12345678a"))
        # Test password with no special character
        self.assertFalse(validate_password("12345678aA"))
        # Test password common password
        self.assertFalse(validate_password("P@ssw0rd"))
        self.assertTrue(validate_password("Along@cceptabl3pAssw8rd"))
