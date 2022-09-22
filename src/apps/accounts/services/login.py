import re

from django.contrib.auth import get_user_model

from src.apps.accounts.functions import login as login_function
from src.apps.accounts.selectors import get_user

User = get_user_model()
email_regex = r"^[\w\-\.]+@([\w-]+\.)+[\w\-]{2,4}$"


def login(authenticator, password):
    try:
        if re.fullmatch(email_regex, authenticator):
            user = get_user(email=authenticator)
        else:
            user = get_user(username=authenticator)
        if user.check_password(password):
            return login_function(user)
    except User.DoesNotExist:
        pass
    return None
