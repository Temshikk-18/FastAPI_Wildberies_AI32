from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from mysite.db.database import SessionLocal
from mysite.db.models import Product
from mysite.db.schema import ProductSchema


product_router = APIRouter(prefix='/product', tags=['Product'])


async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@product_router.post('/create', response_model=ProductSchema)
async def create(data: ProductSchema, db: Session = Depends(get_db)):
    product_db = Product(**data.dict())

    db.add(product_db)
    db.commit()
    db.refresh(product_db)

    return product_db


@product_router.get('/list', response_model=list[ProductSchema])
async def list(db: Session = Depends(get_db)):
    product_db = db.query(Product).all()

    return product_db


@product_router.get('/detail/{product_id}', response_model=ProductSchema)
async def detail(product_id: int, db: Session = Depends(get_db)):
    product_db = db.query(Product).filter(Product.id == product_id).first()

    if not product_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='mynday product jok!')

    return product_db


@product_router.put('/update/{product_id}', response_model=ProductSchema)
async def update(product_id: int, data: ProductSchema, db: Session = Depends(get_db)):
    product_db = db.query(Product).filter(Product.id == product_id).first()

    if not product_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='mynday product jok!!!')

    for key, value in data.dict().items():
        setattr(product_db, key, value)

    db.commit()
    db.refresh(product_db)

    return product_db


@product_router.delete('/delete/{product_id}', response_model=dict)
async def delete(product_id: int, db: Session = Depends(get_db)):
    product_db = db.query(Product).filter(Product.id == product_id).first()

    if not product_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='mynday product jok eken!')

    db.delete(product_db)
    db.commit()

    return {'status': 'Ийгиликтуу очурулду'}


