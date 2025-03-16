from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from .views import CustomerViewSet, ProductViewSet, CollectionViewSet, ReviewViewSet, CartViewSet, CartItemViewSet


router = routers.DefaultRouter()
router.register('products', ProductViewSet, basename='product')
router.register('collections', CollectionViewSet)
router.register('carts', CartViewSet)
router.register('customers', CustomerViewSet)

products_router = routers.NestedSimpleRouter(
    router, 'products', lookup='product')
products_router.register('reviews', ReviewViewSet, basename='product-reviews')

carts_router = routers.NestedSimpleRouter(router, 'carts', lookup='cart')
carts_router.register('items', CartItemViewSet, basename='cart-items')
# URLConf
urlpatterns = [
    path('', include(router.urls + products_router.urls)),
    path('', include(router.urls + carts_router.urls)),
]
