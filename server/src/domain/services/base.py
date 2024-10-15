from typing import List, Mapping, Optional, Type, TypeVar, Any, Generic
from domain.repositories.base import BaseRepository
from domain.models.base import Base
from pydantic import BaseModel


R = TypeVar("R", bound=BaseRepository)
S = TypeVar("S", bound=BaseModel)
T = TypeVar("T", bound=Base)


class BaseService(Generic[R, T]):
    repository: R

    def __init__(self, repository: R):
        self.repository = repository

    def get_all(self) -> List[T]:
        return self.repository.get_all()

    def get_one(self, **filters: Mapping[str, Any]) -> Optional[T]:
        return self.get_one(filters=filters)

    def create(self, data: T) -> None:
        self.repository.create(data)

    def delete(self, **filters: Mapping[str, Any]) -> None:
        self.repository.delete(filters=filters)

    def to_schema(self, data: T, model_type: Type[S]) -> S:
        data_dict = data.__dict__
        return model_type(**data_dict)
