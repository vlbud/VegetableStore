from django.urls import path
from .views import ShopView, CartView, ProductSingleView, CartViewSet, WishlistView #Wishlistdel
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'cart', CartViewSet)

app_name = 'store'
urlpatterns = [
    path('', ShopView.as_view(), name='shop'),
    path('cart/', CartView.as_view(), name='cart'),
    path('product/<int:id>/', ProductSingleView.as_view(), name='product'),
    path('wishlist/', WishlistView.as_view(), name='wishlist'),
    # path('wishlist/del/<int:item_id>', Wishlistdel, name='wishlistdell')

]
