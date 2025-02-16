from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import dataclass

from src.apps.account.services.user import BaseUserService
from src.apps.account.services.otp_gen import BaseOTPService
from src.apps.account.services.senders import BaseSenderService



# TODO: выпилить бизнес логику и перенести её в юзкейсы
@dataclass(eq=False)
class BaseAuthService(ABC):
    user_service: BaseUserService
    codes_service: BaseOTPService
    sender_service: BaseSenderService

    @abstractmethod
    def authorize(self, email: str):
        ...

    @abstractmethod
    def confirm(self, code: str, email: str):
        ...


class AuthService(BaseAuthService):
    def authorize(self, email: str):
        customer = self.user_service.get_or_create(email)
        code = self.codes_service.generate_code(customer)
        self.sender_service.send_code(customer, code)

    def confirm(self, code: str, email: str):
        customer = self.user_service.get(email)
        self.codes_service.validate_code(code, customer)
        return self.user_service.generate_token(customer)