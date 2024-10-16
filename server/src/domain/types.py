from typing import TypeVar
from domain.models import Base


ModelT = TypeVar("ModelT", bound=Base)
