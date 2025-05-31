from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str

class IMC(BaseModel):
    user_id: int
    weight: float
    height: float
    imc_value: float
    created_at: str