from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from mysite.db.database import SessionLocal
from mysite.db.models import Cart
from mysite.db.schema import CartSchema


cart_router = APIRouter(prefix='/cart', tags=['Cart'])


async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@cart_router.post('/create', response_model=CartSchema)
async def create(data: CartSchema, db: Session = Depends(get_db)):
    cart_db = Cart(**data.dict())

    db.add(cart_db)
    db.commit()
    db.refresh(cart_db)

    return cart_db


@cart_router.get('/list', response_model=list[CartSchema])
async def list(db: Session = Depends(get_db)):
    cart_db = db.query(Cart).all()

    return cart_db


@cart_router.get('/detail/{cart_id}', response_model=CartSchema)
async def detail(cart_id: int, db: Session = Depends(get_db)):
    cart_db = db.query(Cart).filter(Cart.id == cart_id).first()

    if not cart_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='mynday cart jok!')

    return cart_db


@cart_router.put('/update/{cart_id}', response_model=CartSchema)
async def update(cart_id: int, data: CartSchema, db: Session = Depends(get_db)):
    cart_db = db.query(Cart).filter(Cart.id == cart_id).first()

    if not cart_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='mynday cart jok!!!')

    for key, value in data.dict().items():
        setattr(cart_db, key, value)

    db.commit()
    db.refresh(cart_db)

    return cart_db


@cart_router.delete('/delete/{cart_id}', response_model=dict)
async def delete(cart_id: int, db: Session = Depends(get_db)):
    cart_db = db.query(Cart).filter(Cart.id == cart_id).first()

    if not cart_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='mynday cart jok eken!')

    db.delete(cart_db)
    db.commit()

    return {'status': 'Ийгиликтуу очурулду'}


