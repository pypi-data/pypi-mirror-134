# Standard Library
import abc
from enum import Enum, auto
from typing import TYPE_CHECKING, Any, List, Optional, Protocol, Type, Union

# External Dependencies
from pydantic import AnyUrl, BaseModel
from pydantic.networks import PostgresDsn, RedisDsn

if TYPE_CHECKING:
    from pydantic.networks import Parts

# Shakah Library
from shakah import logger

# A Url Protocol for SQLite


class EnvType(str, Enum):
    LOCAL = ""
    DEV = "developer"
    PROD = "admin"
