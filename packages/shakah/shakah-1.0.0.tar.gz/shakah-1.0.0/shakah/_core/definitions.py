# Standard Library
import inspect
import uuid
from typing import Any, Callable, Dict, Optional, Tuple, Type, TypeVar, Union

# External Dependencies
import wrapt
from fastcore.basics import annotations
from loguru import logger
from sqlalchemy import or_
from sqlalchemy.engine import Engine
from sqlmodel import Field, Session, SQLModel, select
from sqlmodel.engine.result import Result, ScalarResult
from sqlmodel.main import FieldInfo, SQLModelMetaclass
from sqlmodel.sql.expression import Select, SelectOfScalar

# Shakah Library
from shakah.conn import get_engine, subscribe
from shakah.utils import classproperty
from shakah.utils.decorators.classes import ClassPropertyMetaClass

logger.disable("shakah._core.definitions")

_T = TypeVar("_T")


def __dataclass_transform__(
    *,
    eq_default: bool = True,
    order_default: bool = False,
    kw_only_default: bool = False,
    field_descriptors: Tuple[Union[type, Callable[..., Any]], ...] = (()),
) -> Callable[[_T], _T]:
    return lambda a: a


@wrapt.decorator
def autoselect(wrapped, instance, args, kwargs):
    # logger instance and arg variables
    logger.info(instance)
    return instance.db.exec(wrapped(*args, **kwargs))


def criterion(x):
    if not inspect.isroutine(x):
        return False
    name = x.__name__

    if name.startswith("__") or name.startswith("_"):
        return False

    if name in ["parse_raw", "schema", "schema_json", "parse_file", "construct"]:
        return False
    annos = {}
    try:
        annos = annotations(x)
    except Exception as e:
        logger.error(f"Can't extract annotations for {name}")
        return False
    if not annos:
        return False
    returns = annos.get("return", None)
    if not returns:
        return False
    if returns not in [SelectOfScalar, Select]:
        return False
    return True


@__dataclass_transform__(kw_only_default=True, field_descriptors=(Field, FieldInfo))
class ShakahModelBuiltinMetaclass(SQLModelMetaclass, ClassPropertyMetaClass):
    __engine__: Engine
    __session__: Session
    __updb__: bool = False
    __instance__: Any = None
    __metaname__: str = "ShakahModelMetaclass"

    # create unique id for each model

    def __new__(
        cls,
        name: str,
        bases: Tuple[Type[Any], ...],
        class_dict: Dict[str, Any],
        **kwargs: Any,
    ) -> Any:
        model = super().__new__(cls, name, bases, class_dict, **kwargs)
        model.update_meta()
        subscribe("engine_update", model)
        # create singleton instance
        if not hasattr(model, "__instance__"):
            model.__instance__ = model()

        return model

    @classmethod
    def update_engine(cls):

        setattr(cls, "__engine__", get_engine())
        setattr(cls, "__updb__", True)
        return True

    @classmethod
    def update_session(cls):
        if not getattr(cls, "__session__", None) or cls.__updb__ == True:

            setattr(cls, "__session__", Session(cls.__engine__))
            setattr(cls, "__updb__", False)

    @classproperty
    def engine_(cls):

        return cls.__engine__

    @engine_.setter  # type: ignore
    def engine_(cls, value):
        cls.__engine__ = value

    @classproperty
    def db_(cls):

        return cls.__session__

    @classmethod
    def update_meta(cls):
        cls.update_engine()
        cls.update_session()

    def getty(cls, name: str, default=None):
        return getattr(cls, name, default)

    # putty set attr
    def putty(cls, name: str, value):
        setattr(cls, name, value)

    # Get instance with classproperty

    @classproperty
    def instance_(cls):
        return cls.__instance__

    @classproperty
    def mname(cls):
        return cls.__metaname__


class ShakahProps(SQLModel, metaclass=ShakahModelBuiltinMetaclass):
    __table_args__ = {"extend_existing": True}

    def __init__(self_, **data: Any) -> None:
        super().__init__(**data)
        logger.debug(f"{self_.__class__.__name__}.__init__({data})")
        cls = self_.__class__
        routines = inspect.getmembers(cls, predicate=criterion)
        # Filter for all bound methods and functions
        logger.debug(routines)
        for name, func in routines:
            logger.info((name, func))
            # fn = getattr(cls, name, None)
            # delattr(model, name, None)

            setattr(cls, name, autoselect(func))

    def update(self, data: str):
        # logger.debug("Updating %s with %s" % (self.__class__.__name__, data))
        if data == "metadata":
            logger.info("Updating engine & session")
            self.md.update_meta()

    def instance(self):
        return self.md.instance_

    @property
    def md(s):
        return type(s)

    @property
    def select(self):
        return select(self.md)

    @property
    def engine(s):
        return s.md.engine_

    @property
    def db(s) -> Session:
        return s.md.db_

    @property
    def active(self):
        return self.dict(exclude_none=True, exclude_unset=True, exclude_defaults=True)

    @property
    def is_active(self) -> bool:
        return bool(self.active)

    def find_(s, *args, **kwargs) -> SelectOfScalar:
        # vdict = s.active

        if not s.is_active:
            raise ValueError("No data was inputted into the system.")

        def compare(key, value):
            return getattr(s.md, key) == value

        comparisons = [compare(k, v) for k, v in s.active.items()]

        return s.select.where(or_(*comparisons))

    def sync(self, *args, **kwargs) -> bool:
        # vdict = s.active
        update_data = self.dict(exclude_unset=True)
        first_record = self.find().first()
        if not first_record:
            return False

        first_record.update(update_data)
        self = self.copy(update=first_record)

        return True

    def save(self):
        self.sync()
        self.db.add(self)
        self.db.commit()

    def shift(self):
        first_record = self.find().first()
        if not first_record:
            return False

        # self.md.construct(first_record)

    def find(self, *args, **kwargs) -> Union[ScalarResult, Result]:
        found: ScalarResult = self.find_(*args, **kwargs)  # type: ignore
        return found


class ShakahModel(ShakahProps, SQLModel):

    id: Optional[uuid.UUID] = Field(primary_key=True, default_factory=uuid.uuid4)
