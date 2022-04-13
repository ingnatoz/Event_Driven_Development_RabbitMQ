from rest_framework.routers import DefaultRouter

from apps.products.api.api import *

router = DefaultRouter()
router.register('product', ProductViewSet, basename="product")
router.register('user', UserViewSet, basename="user")
urlpatterns = router.urls
