from abc import ABC, abstractmethod
from app.domain.user import User

class IUserRepository(ABC):

    @abstractmethod
    async def find_by_email(self, email: str) -> User | None:
        pass

    @abstractmethod
    async def create_or_update(self, user: User) -> User:
        pass
