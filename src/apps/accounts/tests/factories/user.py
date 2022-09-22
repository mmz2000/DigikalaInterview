import factory
from django.contrib.auth import get_user_model


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()

    first_name = factory.Faker("name")
    last_name = factory.Faker("name")
    email = factory.Faker("email")
    password = "foo"
    set_password = factory.PostGenerationMethodCall("set_password", "foo")
