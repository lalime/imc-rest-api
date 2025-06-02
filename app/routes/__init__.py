from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services import (
    get_current_user,
    create_user,
    get_user_by_username,
    authenticate_user,
    create_access_token,
    calculate_and_store_imc
)
from app.db import database
from app.models import UserCreate, UserLogin, IMCCreate

router = APIRouter()


@router.post(
    "/register",
    summary="Register a new user",
    description=(
        "Create a new user account by providing a username and password."
    )
)
def register(user: UserCreate, db: Session = Depends(database.get_db)):
    db_user = get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(
            status_code=400, detail="Username already registered"
        )
    return create_user(db=db, user=user)


@router.post(
    "/login",
    summary="User login",
    description="Authenticate a user and return a JWT access token."
)
def login(form_data: UserLogin, db: Session = Depends(database.get_db)):
    user = authenticate_user(
        db,
        form_data.username,
        form_data.password
    )
    if not user:
        raise HTTPException(
            status_code=400,
            detail="Incorrect username or password"
        )
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}


@router.post(
    "/calculate-imc",
    summary="Calculate IMC (BMI)",
    description="Calculate IMC (BMI) for the authenticated user and store the result."
)
def calculate_imc(
    imc: IMCCreate,
    db: Session = Depends(database.get_db),
    user=Depends(get_current_user)
):
    imc_value, result = calculate_and_store_imc(
        db,
        user.id,
        imc.weight,
        imc.height
    )
    return {"imc": imc_value, "result": result}


@router.get(
    "/imc-history/{user_id}",
    summary="Get IMC history",
    description="Retrieve IMC calculation history for a specific user."
)
def get_imc_history(
    user_id: int,
    db: Session = Depends(database.get_db),
    user=Depends(get_current_user)
):
    return get_imc_history(db, user_id)