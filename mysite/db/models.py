from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Enum, ForeignKey, Text, Date, Boolean
from .database import Base
from typing import Optional
from enum import Enum as PyEnum
from datetime import datetime, date


class UserStatus(str, PyEnum):
    gold = 'gold'
    silver = 'silver'
    bronze = 'bronze'
    simple = 'simple'


class SizeChoices(str, PyEnum):
    S = 'S'
    M = 'M'
    L = 'M'
    XL = 'XL'
    XXL = 'XXL'
    XXXL = 'XXXL'



class UserProfile(Base):
    __tablename__ = 'user_profile'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    first_name: Mapped[Optional[str]] = mapped_column(String(32), nullable=True)
    last_name: Mapped[str | None] = mapped_column(String(32), nullable=True)
    username: Mapped[str] = mapped_column(String(32), unique=True)
    email: Mapped[str] = mapped_column(String(32), unique=True)
    age: Mapped[int] = mapped_column(Integer, default=0)
    phone_number: Mapped[str] = mapped_column(String(12), unique=True)
    profile_image: Mapped[str | None] = mapped_column(String(32), nullable=True)
    status: Mapped[UserStatus] = mapped_column(Enum(UserStatus), default=UserStatus.simple)
    password: Mapped[str] = mapped_column(String)

    product_owner: Mapped[list['Product']] = relationship('Product',
                                                          back_populates='owner', cascade='all, delete-orphan')
    review_user: Mapped[list['Review']] = relationship('Review',
                                                       back_populates='user', cascade='all, delete-orphan')
    cart: Mapped['Cart'] = relationship('Cart',
                                        back_populates='user', cascade='all, delete-orphan')
    favorite_user: Mapped[list['Favorite']] = relationship('Favorite',
                                                           back_populates='user', cascade='all, delete-orphan')
    refresh_token: Mapped[list[RefreshToken]] = relationship('RefreshToken',
                                                             back_populates='user', cascade='all, delete-orphan')


class RefreshToken(Base):
    __tablename__ = 'refresh_token'

    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    token: Mapped[str] = mapped_column(String, nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey('user_profile.id'))

    user: Mapped['UserProfile'] = relationship('UserProfile', back_populates='refresh_token')


class Category(Base):
    __tablename__ = 'category'

    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    category_name: Mapped[str] = mapped_column(String(32), unique=True)
    category_image: Mapped[str] = mapped_column(String(32))

    sub_category: Mapped[list['SubCategory']] = relationship('SubCategory',
                                                       back_populates='category', cascade='all, delete-orphan')

    product_category: Mapped[list[Product]] = relationship('Product',
                                                           back_populates='category', cascade='all, delete-orphan')


class SubCategory(Base):
    __tablename__ = 'sub_category'

    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    category_id: Mapped[int] = mapped_column(ForeignKey('category.id'))
    sub_category_name: Mapped[str] = mapped_column(String(32))

    category: Mapped['Category'] = relationship('Category', back_populates='sub_category')
    product_sub: Mapped[list['Product']] = relationship('Product',
                                                        back_populates='sub_category', cascade='all, delete-orphan')


class Product(Base):
    __tablename__ = 'product'

    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    category_id: Mapped[int] = mapped_column(ForeignKey('category.id'))
    sub_category_id: Mapped[int] = mapped_column(ForeignKey('sub_category.id'))
    product_name: Mapped[str] = mapped_column(String(32))
    product_video: Mapped[str] = mapped_column(String)
    product_image: Mapped[str] = mapped_column(String)
    price: Mapped[int] = mapped_column(Integer, default=0)
    chose_size: Mapped[SizeChoices] = mapped_column(Enum(SizeChoices))
    description: Mapped[str] = mapped_column(Text)
    owner_id: Mapped[int] = mapped_column(ForeignKey('user_profile.id'))

    category: Mapped['Category'] = relationship('Category', back_populates='product_category')
    sub_category: Mapped['SubCategory'] = relationship('SubCategory', back_populates='product_sub')
    owner: Mapped['UserProfile'] = relationship('UserProfile', back_populates='product_owner')

    imgs_product: Mapped[list['ImageProduct']] = relationship('ImageProduct',
                                                              back_populates='product', cascade='all, delete-orphan')
    review_product: Mapped[list['Review']] = relationship('Review',
                                                          back_populates='product', cascade='all, delete-orphan')
    item_product: Mapped[list['CartItem']] = relationship('CartItem',
                                                          back_populates='product', cascade='all, delete-orphan')
    favorite_product: Mapped[list['Favorite']] = relationship('Favorite',
                                                              back_populates='product', cascade='all, delete-orphan')


class ImageProduct(Base):
    __tablename__ = 'images_product'

    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    product_id: Mapped[int] = mapped_column(ForeignKey('product.id'))
    image: Mapped[str] = mapped_column(String)

    product: Mapped['Product'] = relationship('Product', back_populates='imgs_product')


class Review(Base):
    __tablename__ = 'review'

    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user_profile.id'))
    product_id: Mapped[int] = mapped_column(ForeignKey('product.id'))
    comment: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    stars: Mapped[int] = mapped_column(Integer, default=0)
    image: Mapped[str | None] = mapped_column(String, nullable=True)
    video: Mapped[str | None] = mapped_column(String, nullable=True)
    created_at: Mapped[date] = mapped_column(Date, default=date.today())

    user: Mapped['UserProfile'] = relationship('UserProfile', back_populates='review_user')
    product: Mapped['Product'] = relationship('Product', back_populates='review_product')


class Cart(Base):
    __tablename__ = 'cart'

    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user_profile.id'), unique=True)

    user: Mapped['UserProfile'] = relationship('UserProfile', back_populates='cart')
    items: Mapped[list['CartItem']] = relationship('CartItem',
                                                   back_populates='cart', cascade='all, delete-orphan')


class CartItem(Base):
    __tablename__ = 'cart_item'

    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    cart_id: Mapped[int] = mapped_column(ForeignKey('cart.id'))
    product_id: Mapped[int] = mapped_column(ForeignKey('product.id'))
    quantity: Mapped[int] = mapped_column(Integer, default=1)

    cart: Mapped['Cart'] = relationship('Cart', back_populates='items')
    product: Mapped['Product'] = relationship('Product', back_populates='item_product')


class Favorite(Base):
    __tablename__ = 'favorite'

    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user_profile.id'))
    product_id: Mapped[int | None] = mapped_column(ForeignKey('product.id'), nullable=True)
    like: Mapped[bool | None] = mapped_column(Boolean, default=False, nullable=True)

    user: Mapped['UserProfile'] = relationship('UserProfile', back_populates='favorite_user')
    product: Mapped['Product'] = relationship('Product', back_populates='favorite_product')












