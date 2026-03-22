from db.models import User
from django.contrib.auth import get_user_model


def create_user(
        username: str,
        password: str,
        email: str = None,
        first_name: str = None,
        last_name: str = None
) -> None:
    optional_params = {}
    if email:
        optional_params["email"] = email
    if first_name:
        optional_params["first_name"] = first_name
    if last_name:
        optional_params["last_name"] = last_name
    user = get_user_model()
    user.objects.create_user(
        username=username,
        password=password,
        **optional_params
    )


def get_user(user_id: int) -> User:
    user = get_user_model()
    return user.objects.get(pk=user_id)


def update_user(
        user_id: int,
        username: str = None,
        password: str = None,
        email: str = None,
        first_name: str = None,
        last_name: str = None
) -> None:
    user = get_user(user_id)
    if username:
        user.username = username
    if password:
        user.set_password(password)
    if email:
        user.email = email
    if first_name:
        user.first_name = first_name
    if last_name:
        user.last_name = last_name
    user.save()
