from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import dataclass
from typing import Iterable

from django.core.mail import send_mail

from src.apps.account.entities import User



class BaseSenderService(ABC):
    @abstractmethod
    def send_code(self, user: User, code: str) -> None:
        ...

# TODO: Implement different verification methods
class EmailSenderService(BaseSenderService):
    def send_code(self, user: User, code: str) -> None:
        subject = 'Ваш код подтверждения'
        message = f'Ваш код подтверждения: {code}'

        send_mail(subject, message, 'noreply@example.com', [user.email])


@dataclass
class ComposedSenderService(BaseSenderService):
    sender_services: Iterable[BaseSenderService]

    def send_code(self, user: User, code: str) -> None:
        for service in self.sender_services:
            service.send_code(user, code)