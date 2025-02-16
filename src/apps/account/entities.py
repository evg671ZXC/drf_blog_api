from dataclasses import (
    dataclass,
    field,
)
from typing import Optional, Union
import datetime
from pathlib import Path


@dataclass
class User:
    id: Optional[int] = field(default=None, kw_only=True)  # noqa
    username: str
    email: str


@dataclass
class Profile:
    id: Optional[int] = field(default=None, kw_only=True)  # noqa
    username: str
    email: str
    bio: Optional[str] = field(default=None)
    location: Optional[str] = field(default=None)
    photo: Optional[Union[str, Path]] = field(default=None) # Path to the photo or URL
    date_of_birth: Optional[datetime.date] = field(default=None)
    # created_at: datetime
    # updated_at: datetime