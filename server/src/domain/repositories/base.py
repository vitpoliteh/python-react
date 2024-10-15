from typing import Mapping, Optional, TypeVar, Generic, Type, List, Any
from sqlalchemy.engine import Engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker
from sqlalchemy import select, create_engine, delete


T = TypeVar("T", bound=DeclarativeBase)

class BaseRepository(Generic[T]):
    engine: Engine
    session: Session
    model_class: Type[T]

    def __init__(self, engine: Engine, model_class: Type[T]):
        self.engine = engine
        session = sessionmaker(bind=self.engine)
        self.session = session()

    def get_all(self) -> List[T]:
        return self.session.query(self.model_class).all()

    def create(self, data: T) -> None:
        self.session.add(data)
        self.session.commit()

    def get_one(self, **filters: Mapping[str, Any]) -> Optional[T]:
        self.__validate_filters(filters=filters)
        return self.session.query(self.model_class).filter_by(**filters).first()

    def delete(self, **filters: Mapping[str, Any]) -> None:
        self.__validate_filters(filters=filters)
        query = self.session.query(self.model_class).filter_by(**filters)
        deleted_count = query.delete()
        self.session.commit()

    def __validate_filters(self, **filters: Mapping[str, Any]) -> None:
        for key in filters.keys():
            if not hasattr(self.model_class, key):
                raise AttributeError(f"Invalid filter field: {key}")
