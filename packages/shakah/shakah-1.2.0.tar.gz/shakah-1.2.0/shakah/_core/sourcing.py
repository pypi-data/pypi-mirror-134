# Standard Library
from typing import TYPE_CHECKING

# External Dependencies
from dynaconf import Dynaconf
from pydantic import BaseSettings, Extra

# Shakah Library
from shakah.dysettings import settings as dyset


class DynaEnabledSettings(BaseSettings):
    class Config:
        case_sensitive = False
        env_file = ".env"
        extra = Extra.allow
        smart_union = True

        @classmethod
        def customise_sources(
            cls,
            init_settings,
            env_settings,
            file_secret_settings,
        ):
            return (
                dynaconf_source,
                init_settings,
                env_settings,
                file_secret_settings,
            )


def dynaconf_source(settings: BaseSettings) -> Dynaconf:
    with dyset.fresh():
        return dyset
