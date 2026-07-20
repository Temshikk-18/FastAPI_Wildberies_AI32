from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from mysite.db.database import SessionLocal
from mysite.db.models import CartItem
from mysite.db.schema import CartItemSchema


cart_item_router = APIRouter(prefix='/cart_item', tags=['CartItem'])


async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@cart_item_router.post('/create', response_model=CartItemSchema)
async def create(data: CartItemSchema, db: Session = Depends(get_db)):
    cart_item_db = CartItem(**data.dict())

    db.add(cart_item_db)
    db.commit()
    db.refresh(cart_item_db)

    return cart_item_db


@cart_item_router.get('/list', response_model=list[CartItemSchema])
async def list(db: Session = Depends(get_db)):
    cart_item_db = db.query(CartItem).all()

    return cart_item_db


@cart_item_router.get('/detail/{cart_id}', response_model=CartItemSchema)
async def detail(cart_id: int, db: Session = Depends(get_db)):
    cart_item_db = db.query(CartItem).filter(CartItem.id == cart_id).first()

    if not cart_item_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='mynday cart jok!')

    return cart_item_db


@cart_item_router.put('/update/{cart_id}', response_model=CartItemSchema)
async def update(cart_item_id: int, data: CartItemSchema, db: Session = Depends(get_db)):
    cart_item_db = db.query(CartItem).filter(CartItem.id == cart_item_id).first()

    if not cart_item_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='mynday cart jok!!!')

    for key, value in data.dict().items():
        setattr(cart_item_db, key, value)

    db.commit()
    db.refresh(cart_item_db)

    return cart_item_db


@cart_item_router.delete('/delete/{cart_id}', response_model=dict)
async def delete(cart_item_id: int, db: Session = Depends(get_db)):
    cart_item_db = db.query(CartItem).filter(CartItem.id == cart_item_id).first()

    if not cart_item_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='mynday cart jok eken!')

    db.delete(cart_item_db)
    db.commit()

    return {'status': 'Ийгиликтуу очурулду'}


