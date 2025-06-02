from sqlalchemy.orm import Session
from app.models import User, IMC, UserCreate
from passlib.context import CryptContext
from tenacity import retry, stop_after_attempt, wait_fixed

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_user_by_username(db: Session, username: str):
    return (
        db.query(User)
        .filter(User.username == username)
        .first()
    )


def create_user(db: Session, user: UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"msg": "User registered"}


def authenticate_user(db: Session, username: str, password: str):
    user = get_user_by_username(db, username)
    if not user or not pwd_context.verify(password, user.hashed_password):
        return False
    return user


@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
def calculate_and_store_imc(db: Session, user_id: int, weight: float, height: float):
    imc_value = weight / (height ** 2)
    if imc_value < 18.5:
        result = "under"
    elif 18.5 <= imc_value <= 24.9:
        result = "normal"
    else:
        result = "over"
    db_imc = IMC(user_id=user_id, weight=weight, height=height, imc_value=imc_value, result=result)
    db.add(db_imc)
    db.commit()
    db.refresh(db_imc)
    return imc_value, result


def get_imc_history(db: Session, user_id: int):
    return db.query(IMC).filter(IMC.user_id == user_id).all()