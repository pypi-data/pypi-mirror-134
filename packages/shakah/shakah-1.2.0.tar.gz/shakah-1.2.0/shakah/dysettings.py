# External Dependencies
from dynaconf import Dynaconf
from dynaconf.loaders import redis_loader
from loguru import logger

# from dynaconf.loaders
settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=[
        "settings.toml",
    ],
    environments=True,
    lowercase_read=True,
    redis_enabled=True,
)
# logger.info(settings.randovalue)


redis_loader.write(
    settings,
    dict(
        SECRET="redis_works",
        POSTGRES_USER="postgres",
        POSTGRES_PASSWORD="postgres",
        POSTGRES_SERVER="localhost",
        POSTGRES_DB="app",
        POSTGRES_DB_TWO="app2",
        POSTGRES_DB_THREE="app3",
        **{"dynaconf_merge": True}
    ),
)

# with settings.using_env("development"):
#     redis_loader.write(settings, {"SECRET": "redis_works_in_dev"})
# `envvar_prefix` = export envvars with `export DYNACONF_FOO=bar`.
# `settings_files` = Load these files in the order.
