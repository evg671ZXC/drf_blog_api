import random
from abc import (
    ABC,
    abstractmethod,
)

from django.core.cache import cache

from src.apps.account.entities import User



class BaseOTPService(ABC):
    @abstractmethod
    def generate_code(self, user: User) -> str:
        ...

    @abstractmethod
    def validate_code(self, code: str, user: User) -> None:
        ...


class CacheCodeService(BaseOTPService):
    def generate_otp(self, user: User) -> str:
        otp_code = str(random.randint(100000, 999999))  # noqa
        cache.set(user.email, otp_code)
        return otp_code

    def validate_code(self, otp_code: str, user: User) -> None:
        cached_code = cache.get(user.email)

        if cached_code is None:
            raise Exception
            # raise Exception(code=otp_code)

        if cached_code != otp_code:
            raise Exception
            # raise Exception(
            #     code=otp_code,
            #     cached_code=cached_code,
            #     customer_phone=user.email,
            # )

        cache.delete(user.email)