from django.test import TestCase

from src.apps.accounts.selectors import user_exists
from src.apps.accounts.tests.factories import UserFactory


class UserExistsSelectorTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.not_saved_user = UserFactory.build()

    def test_user_exists_selector(self):
        self.assertTrue(user_exists(id=self.user.id, email=self.user.email))
        self.assertFalse(
            user_exists(
                id=self.not_saved_user.id, email=self.not_saved_user.email
            )
        )
