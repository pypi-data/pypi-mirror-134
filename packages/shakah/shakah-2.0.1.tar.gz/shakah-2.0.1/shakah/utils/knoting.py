# Standard Library
from typing import TYPE_CHECKING, Any, Protocol

if TYPE_CHECKING:
    pass

# Shakah Library
from shakah import logger
from shakah.gears.structs.vehicles import URIModel
from shakah.typings import PostgresDsn, SqliteUrl

# A Url Protocol for SQLite


def select_uri(scheme: str) -> URIModel:
    return {
        "sqlite": SqliteUrl,
        "postgresql": PostgresDsn,
    }[scheme]


def build_connection_string(scheme: str, data: dict) -> str:
    uri_model = URIModel(url_type=select_uri(scheme), scheme=scheme, **data)
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
