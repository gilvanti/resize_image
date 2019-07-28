from django.urls import path, include
from rest_framework import routers
from resizeimage_rest.viewsets import ImagesViewSet

router = routers.DefaultRouter()
router.register('images', ImagesViewSet, 'images')

app_name = 'resizeimage_rest'
urlpatterns = [
    path('', include(router.urls)),
]
