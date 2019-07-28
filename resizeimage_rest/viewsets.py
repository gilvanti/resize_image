from rest_framework import viewsets, filters
from resizeimage_rest.serializers import ImageSerializer
from resizeimage.models import Image

class ImagesViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
