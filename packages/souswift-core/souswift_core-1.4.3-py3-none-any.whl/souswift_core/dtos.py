import re
from typing import Generic, TypeVar

import pydantic
import pydantic.generics
import ujson

snake_regexp = re.compile(r'_([a-z])')


class Model(pydantic.BaseModel):
    class Config:
        allow_population_by_field_name = True
        json_loads = ujson.loads
        json_dumps = ujson.dumps

        @classmethod
        def alias_generator(cls, field: str):
            return re.sub(snake_regexp, lambda match: match[1].upper(), field)


class FrozenModel(Model):
    class Config(Model.Config):
        allow_mutation = False


T = TypeVar('T', bound=Model)


class BaseResponse(pydantic.generics.GenericModel, Generic[T]):
    data: list[T]


class BaseError(Model):
    title: str
    path: str
    status: int
    detail: str
