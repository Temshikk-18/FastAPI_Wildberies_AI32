from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from mysite.db.database import SessionLocal
from mysite.db.models import Favorite
from mysite.db.schema import FavoriteSchema


favorite_router = APIRouter(prefix='/favorite', tags=['Favorite'])


async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@favorite_router.post('/create', response_model=FavoriteSchema)
async def create(data: FavoriteSchema, db: Session = Depends(get_db)):
    favorite_db = Favorite(**data.dict())

    db.add(favorite_db)
    db.commit()
    db.refresh(favorite_db)

    return favorite_db


@favorite_router.get('/list', response_model=list[FavoriteSchema])
async def list(db: Session = Depends(get_db)):
    favorite_db = db.query(Favorite).all()

    return favorite_db


@favorite_router.get('/detail/{cart_id}', response_model=FavoriteSchema)
async def detail(favorite_id: int, db: Session = Depends(get_db)):
    favorite_db = db.query(Favorite).filter(Favorite.id == favorite_id).first()

    if not favorite_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='mynday favorite jok!')

    return favorite_db


@favorite_router.put('/update/{cart_id}', response_model=FavoriteSchema)
async def update(favorite_id: int, data: FavoriteSchema, db: Session = Depends(get_db)):
    favorite_db = db.query(Favorite).filter(Favorite.id == favorite_id).first()

    if not favorite_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='mynday favorite jok!!!')

    for key, value in data.dict().items():
        setattr(favorite_db, key, value)

    db.commit()
    db.refresh(favorite_db)

    return favorite_db


@favorite_router.delete('/delete/{cart_id}', response_model=dict)
async def delete(favorite_id: int, db: Session = Depends(get_db)):
    favorite_db = db.query(Favorite).filter(Favorite.id == favorite_id).first()

    if not favorite_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='mynday favorite jok eken!')

    db.delete(favorite_db)
    db.commit()

    return {'status': 'Ийгиликтуу очурулду'}


