from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from mysite.db.database import SessionLocal
from mysite.db.models import Review
from mysite.db.schema import ReviewSchema


review_router = APIRouter(prefix='/review', tags=['Review'])


async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@review_router.post('/create', response_model=ReviewSchema)
async def create(data: ReviewSchema, db: Session = Depends(get_db)):
    review_db = Review(**data.dict())

    db.add(review_db)
    db.commit()
    db.refresh(review_db)
    return review_db


@review_router.get('/list', response_model=list[ReviewSchema])
async def list(db: Session = Depends(get_db)):
    review_db = db.query(Review).all()

    return review_db


@review_router.get('/detail/{review_id}', response_model=ReviewSchema)
async def detail(review_id: int, data: ReviewSchema, db: Session = Depends(get_db)):
    review_db = db.query(Review).filter(Review.id == review_id)

    if not review_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='mynday comment jok!')

    return review_db


@review_router.put('/update/{review_id', response_model=ReviewSchema)
async def update(review_id: int, data: ReviewSchema, db: Session = Depends(get_db)):
    review_db = db.query(Review).filter(Review.id == review_id).first()

    if not review_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='mynday comment jok')

    for key, value in data.dict().items():
        setattr(review_db, key, value)

    db.commit()
    db.refresh(review_db)

    return review_db


@review_router.delete('/delete/{review_id}', response_model=dict)
async def delete(review_id: int, db: Session = Depends(get_db)):
    review_db = db.query(Review).filter(Review.id == review_id).first()

    if not review_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='mynday comment jok eken!')

    db.delete(review_id)
    db.commit()

    return {'status': 'Ийгиликтуу очурулду'}







