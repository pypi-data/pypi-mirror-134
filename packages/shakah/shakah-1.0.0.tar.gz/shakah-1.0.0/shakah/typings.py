# Standard Library
from typing import TYPE_CHECKING, Any, Optional, Protocol, Type, Union

# External Dependencies
from pydantic import AnyUrl, BaseModel
from pydantic.networks import PostgresDsn as _PostgresDsn
from pydantic.networks import RedisDsn

if TYPE_CHECKING:
    from pydantic.networks import Parts

# Shakah Library
from shakah import logger

# A Url Protocol for SQLite


class SqliteUrl(AnyUrl):
    allowed_schemes = {"sqlite"}
    host_required = False
    hidden_parts = {"port"}

    @staticmethod
    def get_default_parts(parts: "Parts") -> "Parts":
        {}
        return {
            "domain": "",
            "port": "" if parts["port"] in ["80", None] else parts["port"],
            "path": "/:memory:",
        }


# A Postgresql AnyURL with default parts for localhost
class PostgresDsn(_PostgresDsn):
    @staticmethod
    def get_default_parts(parts: "Parts") -> "Parts":
        return {
            "domain": "localhost" if parts["domain"] in ["", None] else parts["domain"],
            "port": "5432",
            "path": "app" if parts["path"] in ["", None] else parts["path"],
        }


class URIModel(BaseModel):
    url_type: Optional[Type[Union[PostgresDsn, SqliteUrl, RedisDsn, AnyUrl]]] = None
    port: Optional[int] = None
    name: Optional[str] = None
    scheme: Optional[str] = None
    host: Optional[str] = None
    database: Optional[str] = None
    user: Optional[str] = None
    password: Optional[str] = None

    def build(self) -> str:
        parts: Parts = self.dict(exclude={"url_type"})  # type: ignore
        parts["domain"] = parts.pop("host")  # type: ignore
        parts["path"] = parts.pop("database")  # type: ignore
        parts["port"] = str(parts.pop("port"))  # type: ignore
        outcome = self.url_type.apply_default_parts(parts)  # type: ignore
        if self.url_type is not None:
            built = self.url_type.build(
                scheme=str(self.scheme),
                user=str(outcome["user"]),
                password=str(outcome["password"]),
                host=str(outcome["domain"]),
                path=f"/{outcome['path']}",
                port=str(outcome["port"]),
            )
            return str(built)
        raise AttributeError("The URL Scheme Is Not Set")
        # self.url_type.build()


def select_uri(scheme: str) -> URIModel:
    return {
        "sqlite": SqliteUrl,
        "postgresql": PostgresDsn,
    }[scheme]


def build_connection_string(scheme: str, data: dict) -> str:
    uri_model = URIModel(url_type=select_uri(scheme), scheme=scheme, **data)
    logger.info(uri_model)
    built = uri_model.build()
    return built


# -----------------------------------------------------------------------------
#                               Protocols
# -----------------------------------------------------------------------------
class SessionKeep(Protocol):
    def instance(self):
        pass

    # @abc.abstractmethod
    def update(self, data: Any):
        raise NotImplementedError
