from django.contrib.auth import get_user_model

User = get_user_model()


def user_exists(**kwargs):
    return User.objects.filter(**kwargs).exists()
