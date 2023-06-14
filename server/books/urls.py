from django.urls import include, path
from rest_framework import routers
from books.views import BookViewSet

router = routers.DefaultRouter()
router.register(r'book', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
