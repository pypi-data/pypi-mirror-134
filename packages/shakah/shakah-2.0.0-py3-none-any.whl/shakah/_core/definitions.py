# Standard Library
from functools import cached_property
import inspect
import uuid
from typing import Any, Callable, Dict, List, Optional, Set, Tuple, Type, TypeVar, Union
# from sqlmodel.main import ModelField

# External Dependencies
import wrapt
from fastcore.basics import annotations, properties
from loguru import logger
from sqlalchemy import func, or_
from sqlalchemy.engine import Engine
from sqlmodel import Field, Session, SQLModel, select
from sqlmodel.engine.result import Result, ScalarResult
from sqlmodel.main import FieldInfo, ModelField, SQLModelMetaclass
from sqlmodel.sql.expression import Select, SelectOfScalar

# Shakah Library
from shakah.conn import get_engine, subscribe
from shakah.errors import RecordExistError
from shakah.utils import classproperty
from shakah.utils.decorators.classes import ClassPropertyMetaClass
from toolz import valfilter, itemfilter
# logger.disable("shakah._core.definitions")

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
    return instance.db.exec(wrapped(*args, **kwargs))


@wrapt.decorator
def unwrapfirst(wrapped, instance, args, kwargs):
    # logger instance and arg variables
    res = wrapped(*args, **kwargs)
    if not res:
        return res
    return res.first()


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

    def update(self, data: str):
        if data == "metadata":
            logger.info("Updating engine & session")
            self.md.update_meta()


def is_foreign_key(x: ModelField):
    info = x.field_info
    return getattr(info, "foreign_key", None) is not None

class ShakahProps(SQLModel, metaclass=ShakahModelBuiltinMetaclass):
    __table_args__ = {"extend_existing": True}
    __find_excludes__ = set()
    
    
    def __init__(self_, **data: Any) -> None:
        super().__init__(**data)

    @property
    def md(s):
        return type(s)

    @property
    def foriegn_keys(s):
        return list(valfilter(is_foreign_key, type(s).__fields__).keys())

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

    @property
    def properties(self) -> Set[str]:
        return set(self.__fields__.keys()) | set(self.__sqlmodel_relationships__.keys())
    
    def binops(self, exclude={"id"}) -> List[Any]:
        def compare(key, value):
            return getattr(self.md, key) == value
        bins = []
        
        for k, v in self.active.items():
            if k in (exclude | self.__find_excludes__) or isinstance(v, (self.md)) or k in self.foriegn_keys:
                continue
            bins.append(compare(k, v))
        return bins

    @autoselect
    def find_(self, *args, exclude={"id"}, **kwargs) -> SelectOfScalar:
        if not self.is_active:
            raise ValueError("No data was inputted into the system.")
        return self.select.where(or_(*self.binops(exclude=exclude)))

# def syncfilter(item) -> bool:
#     x, y = item
#     return (x in syncable) and y is not None


class ShakahModel(ShakahProps, SQLModel):
    
    id: Optional[int] = Field(None, primary_key=True)

    @unwrapfirst
    @autoselect
    def count(self):
        return select(func.count()).select_from(self.md)

    @unwrapfirst
    @autoselect
    def count_match(self, exclude={"id"}):
        if not self.is_active:
            raise ValueError("No data was inputted into the system.")
        return (
            select(func.count())
            .select_from(self.md)
            .where(or_(*self.binops(exclude=exclude)))
        )

    def sync(self, exclude={"id"}) -> None:
        existing = self.find(exclude=(exclude | {"id"})).first()
        if not existing:
            self.save()
            logger.info("Record doesn't exist yet. Creating new record.")
            return
        syncable = self.properties - {"id"}
        def syncfilter(item) -> bool:
            x, y = item
            return (x in (syncable)) and y is not None
        
        update_data = itemfilter(syncfilter, self.__dict__)
        
        for k, v in update_data.items():
            setattr(existing, k, v)
        self.db.add(existing)
        self.db.commit()
        self.db.refresh(existing)
        syncable.add("id")
        self.__dict__.update(existing.__dict__)
        # for k, v in itemfilter(syncfilter, existing.__dict__).items():
        #     setattr(self, k, v)
        return self
        

    def save(self):

        self.db.add(self)
        self.db.commit()
        self.db.refresh(self)

    def delete(self, *args, **kwargs):
        record = self.find().first(*args, **kwargs)
        if not record:
            raise RecordExistError("Record not found.")
        # with self.db as db:
        self.db.delete(record)

    def shift(self):
        first_record = self.find().first()
        if not first_record:
            return False

    def find(self, *args, **kwargs) -> Union[ScalarResult, Result]:
        found: ScalarResult = self.find_(*args, **kwargs)  # type: ignore
        return found

    def find_by_id(self, id: str):
        return self.md(id=id).find_(exclude=set()).first()
