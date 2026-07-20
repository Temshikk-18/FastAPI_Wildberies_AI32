from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from mysite.db.database import SessionLocal
from mysite.db.models import SubCategory
from mysite.db.schema import SubCategorySchema

sub_category_router = APIRouter(prefix='/sub_category', tags=['SubCategory'])


async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@sub_category_router.post('/create', response_model=SubCategorySchema)
async def create(data: SubCategorySchema, db: Session = Depends(get_db)):
    sub_category_db = SubCategory(**data.dict())

    db.add(sub_category_db)
    db.commit()
    db.refresh(sub_category_db)

    return sub_category_db

@sub_category_router.get('/list', response_model=list[SubCategorySchema])
async def list(db: Session = Depends(get_db)):
    sub_category_db = db.query(SubCategory).all()

    return sub_category_db


@sub_category_router.get('/detail/sub_category_id}', response_model=SubCategorySchema)
async def detail(sub_category_id: int, db: Session = Depends(get_db)):
    sub_category_db = db.query(SubCategory).filter(SubCategory.id == sub_category_id).first()

    if not sub_category_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='mynday subcategory jok!')

    return sub_category_db


@sub_category_router.put('/update/{user_id', response_model=SubCategorySchema)
async def update(sub_category_id: int, data: SubCategorySchema, db: Session = Depends(get_db)):
    sub_category_db = db.query(SubCategory).filter(SubCategory.id == sub_category_id).first()

    if not sub_category_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='mynday subcategory jok!')

    for key, value in data.dict().items():
        setattr(sub_category_db, key, value)

    db.commit()
    db.refresh(sub_category_db)

    return sub_category_db


@sub_category_router.delete('/delete/{sub_category_id}', response_model=dict)
async def delete(sub_category_id: int, db: Session = Depends(get_db)):
    sub_category_db = db.query(SubCategory).filter(SubCategory.id == sub_category_id).first()

    if not sub_category_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='mynday subcategory jok!')

    db.delete(sub_category_db)
    db.commit()

    return {'status': 'Ийгиликтуу очурулду'}
