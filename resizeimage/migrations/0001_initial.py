# Generated by Django 2.2.3 on 2019-07-26 15:58

from django.db import migrations, models
import resizeimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=resizeimage.models.scramble_uploaded_filename, verbose_name='Uploaded image')),
            ],
        ),
    ]
