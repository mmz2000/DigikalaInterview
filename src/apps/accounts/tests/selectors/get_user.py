from django.test import TestCase

from src.apps.accounts.selectors import get_user
from src.apps.accounts.tests.factories import UserFactory


class GetUserSelectorTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()

    def test_get_user_selector(self):
        user = get_user(
            id=self.user.id, email=self.user.email, username=self.user.username
        )
        self.assertEqual(user, self.user)
