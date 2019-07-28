from __future__ import absolute_import

import logging
from django.contrib.auth import get_user_model
from resize_backend.celery import app
from celery import shared_task
import os
from resize_backend import settings
from PIL import Image
from django.db import models
from django.db.models import signals


@app.task
def fila(input_image):
    if not input_image or input_image == "":
        return

    resize(input_image.replace('"',''))

def resize(name, size=(384, 384)):

    image = Image.open(os.path.join(settings.MEDIA_ROOT, name))

    image = image.resize(size, Image.ANTIALIAS)

    image.save(os.path.join(settings.MEDIA_ROOT, name))
