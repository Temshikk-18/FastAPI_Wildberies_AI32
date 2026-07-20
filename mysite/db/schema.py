from pydantic import BaseModel
from typing import Optional
from .models import SizeChoices, UserStatus


class UserProfileSchema(BaseModel):
    first_name: str | None
    last_name: Optional[str]
    username: str
    email: str
    age: int | None
    phone_number: str
    status: UserStatus
    profile_image: str | None
    password: str


class RegisterSchema(BaseModel):
    first_name: str | None
    last_name: Optional[str]
    username: str
    phone_number: str
    email: str
    password: str


class LoginSchema(BaseModel):
    username: str
    password: str


class CategorySchema(BaseModel):
    category_name: str
    category_image: str


class SubCategorySchema(BaseModel):
    category_id: int
    sub_category_name: str


class ProductSchema(BaseModel):
    category_id: int
    sub_category_id: int
    product_name: str
    product_video: str
    product_image: str
    price: int
    chose_size: SizeChoices
    description: str
    owner_id: int


class ImageProductSchema(BaseModel):
    product_id: int
    image: str


class ReviewSchema(BaseModel):
    user_id: int
    product_id: int
    comment: Optional[str]
    stars: int
    image: str | None
    video: str | None


class CartSchema(BaseModel):
    user_id: int


class CartItemSchema(BaseModel):
    cart_id: int
    product_id: int
    quantity: int


class FavoriteSchema(BaseModel):
    user_id: int
    product_id: int
    like: bool

