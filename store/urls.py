from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from .views import ProductViewSet, CollectionViewSet, ReviewViewSet


router = routers.DefaultRouter()
router.register('products', ProductViewSet, basename='product')
router.register('collections', CollectionViewSet)

products_router = routers.NestedSimpleRouter(
    router, 'products', lookup='product')
products_router.register('reviews', ReviewViewSet, basename='product-reviews')
# URLConf
urlpatterns = router.urls + products_router.urls
