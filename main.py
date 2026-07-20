from fastapi import FastAPI
from mysite.api import (category, user_profile, sub_category, product,
                        image_product, review, cart, cart_item, favorite, auth)


wildberies_app = FastAPI(title='FastAPI Wildberies')
wildberies_app.include_router(category.category_router)
wildberies_app.include_router(user_profile.user_router)
wildberies_app.include_router(auth.auth_router)
wildberies_app.include_router(sub_category.sub_category_router)
wildberies_app.include_router(product.product_router)
wildberies_app.include_router(image_product.image_product_router)
wildberies_app.include_router(review.review_router)
wildberies_app.include_router(cart.cart_router)
wildberies_app.include_router(cart_item.cart_item_router)
wildberies_app.include_router(favorite.favorite_router)


