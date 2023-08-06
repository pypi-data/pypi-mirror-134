# Standard Library
import inspect
from typing import Any, Callable, Dict, Optional, Tuple, Type, TypeVar, Union

# External Dependencies
import wrapt
from fastcore.basics import annotations
from loguru import logger
from sqlalchemy import or_
from sqlalchemy.future.engine import Engine
from sqlmodel import Field, Session, SQLModel, select
from sqlmodel.engine.result import Result, ScalarResult
from sqlmodel.main import FieldInfo, SQLModelMetaclass
from sqlmodel.sql.expression import Select, SelectOfScalar

# Shakah Library
from shakah import ShakahModel
from shakah.conn import get_engine, push_event, subscribe
from shakah.utils import classproperty
from shakah.utils.decorators.classes import ClassPropertyMetaClass


class ExampleModel(ShakahModel):

    post_text: str = Field(None, index=True)

    class Config:
        table = True
        extend_existing = True


def main():

    SQLModel.metadata.create_all(ShakahModel.engine_)
    built = ExampleModel(post_text="Hello World")
    logger.info(built)
    built.save()
    logger.info(built)
    # found.first()
    # debug(found.one())
    push_event("engine_update", "metadata")


if __name__ == "__main__":
    main()
