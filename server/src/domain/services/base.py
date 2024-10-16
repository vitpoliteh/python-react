from typing import List, Mapping, Optional, Type, TypeVar, Any, Generic
from domain.repositories import BaseRepository
from domain.types import ModelT
from pydantic import BaseModel
from domain.database import engine


R = TypeVar("R", bound=BaseRepository)
S = TypeVar("S", bound=BaseModel)


class BaseService(Generic[ModelT]):
    repository_type: Type[BaseRepository[ModelT]]

    def __init__(self):
        self.repository = self.repository_type(
            engine=engine,
        )

    def get_all(self) -> List[ModelT]:
        return self.repository.get_all()

    def get_one(self, **filters: Mapping[str, Any]) -> Optional[ModelT]:
        return self.get_one(filters=filters)

    def create(self, data: ModelT) -> None:
        self.repository.create(data)

    def delete(self, **filters: Mapping[str, Any]) -> None:
        self.repository.delete(filters=filters)

    def to_schema(self, data: ModelT, model_type: Type[S]) -> S:
        data_dict = data.__dict__
        return model_type(**data_dict)
