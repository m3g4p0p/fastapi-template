from pydantic import BaseModel


class UserModel(BaseModel):

    name: str
    age: int
