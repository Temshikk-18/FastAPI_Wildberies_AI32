from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from mysite.db.database import SessionLocal
from mysite.db.models import Category
from mysite.db.schema import CategorySchema


category_router = APIRouter(prefix='/category', tags=['Category'])

async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@category_router.post('/create', response_model=CategorySchema)
async def create(data: CategorySchema, db: Session = Depends(get_db)):
    category_db = Category(category_name=data.category_name, category_image=data.category_image)
    db.add(category_db)
    db.commit()
    db.refresh(category_db)
    return category_db


@category_router.get('/list', response_model=list[CategorySchema])
async def list(db: Session = Depends(get_db)):
    category_db = db.query(Category).all()
    return category_db


@category_router.get('/detail/{category_id}', response_model=CategorySchema)
async def detail(category_id: int, db: Session = Depends(get_db)):
    category_db = db.query(Category).filter(Category.id == category_id).first()

    if not category_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Mynday category jok')

    return category_db


@category_router.put('/update/{category_id}', response_model=CategorySchema)
async def update(category_id: int,data: CategorySchema, db: Session = Depends(get_db)):
    category_db = db.query(Category).filter(Category.id == category_id).first()

    if not category_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='mynday category jok')

    category_db.category_name = data.category_name
    category_db.category_image = data.category_image

    db.commit()
    db.refresh(category_db)

    return category_db


@category_router.delete('/delete/{category_id}', response_model=dict)
async def delete(category_id: int, db: Session = Depends(get_db)):
    category_db = db.query(Category).filter(Category.id == category_id).first()

    if not category_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='mynday category jok eken')

    db.delete(category_db)
    db.commit()

    return {'status': 'success deleted'}




