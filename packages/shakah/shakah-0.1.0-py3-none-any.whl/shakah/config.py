# Standard Library
from typing import TYPE_CHECKING, Any, Dict, Optional, Union

# External Dependencies
from pydantic import AnyUrl, PostgresDsn, validator

# Shakah Library
from shakah._core.sourcing import DynaEnabledSettings
from shakah.typings import SqliteUrl
from shakah.utils.knoting import build_connection_string


class Settings(DynaEnabledSettings):

    PORT: int
    NAME: str
    SCHEME: str
    HOST: str
    DATABASE: str
    USER: str
    PASSWORD: str

    DATABASE_URI: Union[SqliteUrl, PostgresDsn, AnyUrl, str, None] = None

    @validator("DATABASE_URI", pre=True)
    def generate_url(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        lower_values = {k.lower(): v for k, v in values.items()}
        scheme = lower_values.pop("scheme")
        return build_connection_string(scheme, lower_values)


settings = Settings()
