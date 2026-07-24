from .view import (UserProfileView, CategoryView, SubCategoryView, ProductView, ImageProductView,
                   RefreshTokenView, CartView, CartItemView, ReviewView, FavoriteView)
from fastapi import FastAPI
from sqladmin import Admin
from mysite.db.database import engine

def setup(app: FastAPI):
    admin = Admin(app, engine=engine)
    admin.add_view(UserProfileView)
    admin.add_view(CategoryView)
    admin.add_view(SubCategoryView)
    admin.add_view(ProductView)
    admin.add_view(ImageProductView)
    admin.add_view(RefreshTokenView)
    admin.add_view(CartView)
    admin.add_view(CartItemView)
    admin.add_view(ReviewView)
    admin.add_view(FavoriteView)