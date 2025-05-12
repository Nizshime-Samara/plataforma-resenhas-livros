from pydantic import BaseModel, EmailStr
from typing import Optional

#Modelo de dominio para usuário
class User(BaseModel):
    email: EmailStr
    name: str
    picture: Optional[str] = None