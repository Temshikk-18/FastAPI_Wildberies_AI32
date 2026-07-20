from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from mysite.db.database import SessionLocal
from mysite.db.models import UserProfile
from mysite.db.schema import UserProfileSchema


user_router = APIRouter(prefix='/user', tags=['UserProfile'])


async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# @user_router.post('/create', response_model=UserProfileSchema)
# async def create(data: UserProfileSchema, db: Session = Depends(get_db)):
#     user_db = UserProfile(**data.dict())
#
#     db.add(user_db)
#     db.commit()
#     db.refresh(user_db)
#
#     return user_db


@user_router.get('/list', response_model=list[UserProfileSchema])
async def list(db: Session = Depends(get_db)):
    user_db = db.query(UserProfile).all()

    return user_db


@user_router.get('/detail/{user_id}', response_model=UserProfileSchema)
async def detail(user_id: int, db: Session = Depends(get_db)):
    user_db = db.query(UserProfile).filter(UserProfile.id == user_id).first()

    if not user_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Mynday adam jok eken!')

    return user_db


@user_router.put('/update/{user_id}', response_model=UserProfileSchema)
async def update(user_id: int, data: UserProfileSchema, db: Session = Depends(get_db)):
    user_db = db.query(UserProfile).filter(UserProfile.id == user_id).first()

    if not user_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Mynday adam jok eken!')

    for key, value in data.dict().items():
        setattr(user_db, key, value)

    db.commit()
    db.refresh(user_db)

    return user_db


@user_router.delete('/delete/{user_id}', response_model=dict)
async def delete(user_id: int, db: Session = Depends(get_db)):
    user_db = db.query(UserProfile).filter(UserProfile.id == user_id).first()

    if not user_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Mynday adam jok eken!')

    db.delete(user_db)
    db.commit()

    return {'status': 'Ийгиликтуу очурулду'}

