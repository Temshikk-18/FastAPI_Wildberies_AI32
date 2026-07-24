from mysite.db.models import (Cart, CartItem, Category, Favorite,
                              ImageProduct, Product, Review, SubCategory, UserProfile, RefreshToken)

from sqladmin import ModelView

class UserProfileView(ModelView, model=UserProfile):
    column_list = [UserProfile.id, UserProfile.username]

class CategoryView(ModelView, model=Category):
    column_list = [Category.id, Category.category_name]

class SubCategoryView(ModelView, model=SubCategory):
    column_list = [SubCategory.id, SubCategory.sub_category_name]

class ProductView(ModelView, model=Product):
    column_list = [Product.id, Product.product_name, Product.product_image, Product.product_video]

class ImageProductView(ModelView, model=ImageProduct):
    column_list = [ImageProduct.id, ImageProduct.image]

class ReviewView(ModelView, model=Review):
    column_list = [Review.id, Review.comment, Review.stars, Review.image]

class CartView(ModelView, model=Cart):
    column_list = [Cart.id]

class CartItemView(ModelView, model=CartItem):
    column_list = [CartItem.id]

class FavoriteView(ModelView, model=Favorite):
    column_list = [Favorite.id, Favorite.like]

class RefreshTokenView(ModelView, model=RefreshToken):
    column_list = [RefreshToken.id, RefreshToken.token]
