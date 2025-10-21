from django.db import models
from django.core.validators import FileExtensionValidator

from category.utils import check_image_size


class Doctor(models.Model):
    full_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='doctor/', validators=[
        FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'svg', 'webp']), check_image_size], blank=True,
                              null=True)
    profession = models.CharField(max_length=100)
    experience = models.IntegerField()
    speciality = models.CharField(max_length=200)
    operations = models.IntegerField(null=True, blank=True)
    achievements = models.CharField(max_length=100, null=True, blank=True)
    about = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.full_name
