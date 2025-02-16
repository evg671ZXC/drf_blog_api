from abc import ABC, abstractmethod
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework_simplejwt.exceptions import InvalidToken

from src.apps.account.entities import User as UserEntity
from src.apps.account.models import User as UserModel



class BaseUserService(ABC):
    @abstractmethod
    def get_or_create(self, phone: str) -> UserEntity:
        ...

    @abstractmethod
    def generate_token(self, customer: UserEntity) -> str:
        ...

    @abstractmethod
    def get(self, phone: str) -> UserEntity:
        ...

    @abstractmethod
    def get_by_token(self, token: str) -> UserEntity:
        ...


class UserService(BaseUserService):

    def get_or_create(self, email: str) -> UserEntity:
        user, _ = UserModel.objects.get_or_create(email=email)
        return user

    def generate_token(self, user: UserEntity) -> str:
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)

    def get(self, email: str) -> UserEntity:
        try:
            return UserModel.objects.get(email=email)
        except UserModel.DoesNotExist as e:
            raise ValueError(f"User with email {email} not found") from e

    def get_by_token(self, token: str) -> UserEntity:
        try:
            access_token = AccessToken(token)
            user_id = access_token.payload.get('user_id')
            return UserModel.objects.get(id=user_id)
        except (InvalidToken, UserModel.DoesNotExist) as e:
            raise ValueError("Invalid or expired token") from e