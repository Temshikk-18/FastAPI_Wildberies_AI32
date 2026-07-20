from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from mysite.db.database import SessionLocal
from mysite.db.models import ImageProduct
from mysite.db.schema import ImageProductSchema


image_product_router = APIRouter(prefix='/image_product', tags=['ImageProduct'])


async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@image_product_router.post('/create', response_model=ImageProductSchema)
async def create(data: ImageProductSchema, db: Session = Depends(get_db)):
    image_product_db = ImageProduct(**data.dict())

    db.add(image_product_db)
    db.commit()
    db.refresh(image_product_db)

    return image_product_db


@image_product_router.get('/list', response_model=list[ImageProductSchema])
async def list(db: Session = Depends(get_db)):
    image_product_db = db.query(ImageProduct).all()

    return image_product_db


@image_product_router.get('/detail/{product_id}', response_model=ImageProductSchema)
async def detail(image_product_id: int, db: Session = Depends(get_db)):
    image_product_db = db.query(ImageProduct).filter(ImageProduct.id == image_product_id).first()

    if not image_product_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='mynday productun fotosu jok!')

    return image_product_db


@image_product_router.put('/update/{product_id}', response_model=ImageProductSchema)
async def update(image_product_id: int, data: ImageProductSchema, db: Session = Depends(get_db)):
    image_product_db = db.query(ImageProduct).filter(ImageProduct.id == image_product_id).first()

    if not image_product_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='mynday productun fotosu jok!!!')

    for key, value in data.dict().items():
        setattr(image_product_db, key, value)

    db.commit()
    db.refresh(image_product_db)

    return image_product_db


@image_product_router.delete('/delete/{product_id}', response_model=dict)
async def delete(image_product_id: int, db: Session = Depends(get_db)):
    image_product_db = db.query(ImageProduct).filter(ImageProduct.id == image_product_id).first()

    if not image_product_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='mynday productun fotosu jok eken!')

    db.delete(image_product_db)
    db.commit()

    return {'status': 'Ийгиликтуу очурулду'}


