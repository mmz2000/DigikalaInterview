from datetime import timedelta

from django.test import TestCase
from django.utils import timezone
from freezegun import freeze_time

from src.apps.accounts.functions import validate_token
from src.apps.accounts.services import login_by_id, refresh
from src.apps.accounts.tests.factories import UserFactory


class RefreshServiceTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()

    def test_refresh_token_jwt_function(self):
        tokens = login_by_id(self.user.id)
        with freeze_time(timezone.now() + timedelta(seconds=2)):
            new_tokens = refresh(tokens.get("refresh_token"))
        self.assertTrue(validate_token(new_tokens.get("access_token")))
        self.assertTrue(validate_token(new_tokens.get("refresh_token")))
        self.assertNotEqual(
            tokens.get("access_token"), new_tokens.get("access_token")
        )
