from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import BookViewSet

router = DefaultRouter()
# Register API viewsets here if needed
router.register(r'books', BookViewSet, basename='book')

urlpatterns = [
    path('', include(router.urls)),
]
