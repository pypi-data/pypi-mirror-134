# Standard Library
import uuid
from typing import Optional

# External Dependencies
from loguru import logger
from pydantic import Extra
from pydantic.networks import EmailStr
from pydantic.types import conint, constr
from sqlmodel.main import Relationship, SQLModel

# Shakah Library
from shakah import Field, ShakahModel


class UserTest(ShakahModel, table=True):
    email: EmailStr
    email_verified: bool
    name: str
    given_name: str
    family_name: str
    preferred_username: str
    nickname: str
    token_id: Optional[int] = Field(default=None, foreign_key="oauthtokentest.id")


class OAuthTokenTest(ShakahModel, table=True):
    name: str
    token_type: str
    access_token: str
    refresh_token: str
    expires_at: conint(gt=0)

    class Config:
        extra = Extra.ignore

    def to_token(self):
        return dict(
            access_token=self.access_token,
            token_type=self.token_type,
            refresh_token=self.refresh_token,
            expires_at=self.expires_at,
        )
