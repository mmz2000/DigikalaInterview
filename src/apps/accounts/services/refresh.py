from src.apps.accounts.functions import refresh as refresh_function


def refresh(token):
    access_token, refresh_token = refresh_function(token)
    return {"access_token": access_token, "refresh_token": refresh_token}
