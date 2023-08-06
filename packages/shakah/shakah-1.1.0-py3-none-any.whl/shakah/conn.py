# Standard Library
import abc
import inspect
from typing import Any, Callable, Dict, List, Optional, Tuple, Type, TypeVar, Union

# External Dependencies
from decorator import decorator
from pydantic import BaseModel
from pydantic.main import ModelMetaclass
from sqlalchemy import or_
from sqlalchemy.future.engine import Engine
from sqlmodel import Field, Session, SQLModel, create_engine, select
from sqlmodel.main import FieldInfo, SQLModelMetaclass, resolve_annotations

# Shakah Library
from shakah import logger, typings
from shakah.config import settings
from shakah.utils import classproperty
from shakah.utils.decorators.classes import (
    ClassPropertyDescriptor,
    ClassPropertyMetaClass,
)

logger.disable("shakah.conn")


EXISTING_ENGINE = None
SUBSCRIBERS: Dict[str, List[Type[typings.SessionKeep]]] = {}
SUBSCRIBER_SET = set()


def sublen() -> int:
    return len(SUBSCRIBER_SET)


def subscribe(event_type: str, cls_: Type[Any]):
    setlen = sublen()
    if hasattr(cls_, "mname"):
        SUBSCRIBER_SET.add(cls_.mname)
        if sublen() == setlen:
            return
    logger.warning(f"Subscribing - {cls_.__name__}")
    global SUBSCRIBERS
    if not event_type in SUBSCRIBERS:
        SUBSCRIBERS[event_type] = []
    SUBSCRIBERS[event_type].append(cls_)


def push_event(event_type: str, data: Any):
    global SUBSCRIBERS
    if not event_type in SUBSCRIBERS:
        SUBSCRIBERS[event_type] = []
        return
    event_subscribers = SUBSCRIBERS.get(event_type, [])
    for subscriber in event_subscribers:
        logger.success(subscriber)
        subscriber().update(data)  # type: ignore


def set_engine(engine_: Optional[Engine]):
    global EXISTING_ENGINE
    EXISTING_ENGINE = engine_ or create_engine(str(settings.DATABASE_URI))
    push_event("engine_update", "metadata")


def get_engine() -> Engine:

    # Update the engine every time you change the parameters. Register to model to change engine.
    global EXISTING_ENGINE
    if EXISTING_ENGINE is None:
        EXISTING_ENGINE = create_engine(str(settings.DATABASE_URI))
    return EXISTING_ENGINE
