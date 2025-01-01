from pydantic import BaseModel


class UserIn(BaseModel):
    first_name: str
    last_name: str
    mail: str
    age: int


class UserOut(BaseModel):
    first_name: str
    last_name: str


class TransactionIn(BaseModel):
    city: str
    date: str
    day: str
    description: str
    degree: float


class TransactionOut(BaseModel):
    date: str
    day: str
    description: str
    degree: float
