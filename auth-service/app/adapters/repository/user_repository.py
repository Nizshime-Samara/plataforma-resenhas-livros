from app.adapters.mongo_conn import db
from app.domain.user import User
from app.interfaces.iuser_repository import IUserRepository

class UserRepository(IUserRepository):

    def __init__(self):
        self.collection = db["users"]

    async def find_by_email(self, email: str) -> User | None:
        user_data = await self.collection.find_one({"email": email})
        return User(**user_data) if user_data else None

    async def create_or_update(self, user: User) -> User:
        await self.collection.update_one(
            {"email": user.email},
            {"$set": user.dict()},
            upsert=True
        )
        return user
    
    async def list_all(self) -> list[User]:
        users = []
        async for doc in self.collection.find():
            users.append(User(**doc))
        return users