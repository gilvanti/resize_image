import uuid
import os
from resize_backend import settings
from django.db import models
from resize_backend.tasks import fila
from django.db.models import signals
import json

def scramble_uploaded_filename(instance, filename):
    extension = filename.split(".")[-1]
    return "{}.{}".format(uuid.uuid4(), extension)


class Image(models.Model):
    image = models.ImageField("Uploaded image", upload_to=scramble_uploaded_filename)

    def save(self, *args, **kwargs):
        super(Image, self).save(*args, **kwargs)
        fila.delay(json.dumps(str(self.image)))
