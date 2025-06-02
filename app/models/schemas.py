"# This file defines the Pydantic models for request and response schemas"
from datetime import datetime
from pydantic import BaseModel


class UserCreate(BaseModel):
    """User information associated with the IMC calculation."""
    username: str
    password: str


class UserLogin(BaseModel):
    username: str
    password: str


class IMCCreate(BaseModel):
    weight: float
    height: float


class IMCOut(BaseModel):
    imc: float
    result: str
    """IMC calculation output model."""
    class Config:
        orm_mode = True


class IMCResponse(BaseModel):
    """Response model for IMC calculations."""
    user_id: int
    weight: float
    height: float
    imc_value: float
    result: str
    created_at: str
    

class IMCHistoryResponse(BaseModel):
    imc: float
    result: str
    created_at: datetime