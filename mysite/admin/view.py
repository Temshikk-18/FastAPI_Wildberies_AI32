from mysite.db.models import (Cart, CartItem, Category, Favorite,
                              ImageProduct, Product, Review, SubCategory, UserProfile, RefreshToken)

from sqladmin import ModelView

class UserProfileView(ModelView):
    column_list = [UserProfile.id, UserProfile.username]

class CategoryView(ModelView):
    column_list = [Category.id, Category.category_name]

class SubCategoryView(ModelView):
    column_list = [SubCategory.id, SubCategory.sub_category_name]

class ProductView(ModelView):
    column_list = [Product.id, Product.product_name, Product.product_image, Product.product_video]

class ImageProductView(ModelView):
    column_list = [ImageProduct.id, ImageProduct.image]

class ReviewView(ModelView):
    column_list = [Review.id, Review.comment, Review.stars, Review.image]

class CartView(ModelView):
    column_list = [Cart.id]

class CartItemView(ModelView):
    column_list = [CartItem.id]

class FavoriteView(ModelView):
    column_list = [Favorite.id, Favorite.like]

class RefreshTokenView(ModelView):
    column_list = [RefreshToken.id, RefreshToken.token]
