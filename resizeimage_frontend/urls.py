from django.urls import path, include
from django.views.generic.base import RedirectView


app_name = 'resizeimage_rest'
urlpatterns = [
    path('', RedirectView.as_view(url='static/index.html', permanent=False), name='index')
]
