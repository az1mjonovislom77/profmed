from django.db import models
from django.core.validators import FileExtensionValidator

from category.utils import check_image_size


class HomepageStats(models.Model):
    happy_patients = models.PositiveIntegerField()
    wards = models.PositiveIntegerField()
    awards = models.PositiveIntegerField()
    ambulances = models.PositiveIntegerField()

    def __str__(self):
        return str(self.happy_patients)


class FooterStats(models.Model):
    doctors = models.PositiveIntegerField()
    experience = models.PositiveIntegerField()
    awards = models.PositiveIntegerField()
    successfully_operations = models.PositiveIntegerField()

    def __str__(self):
        return str(self.doctors)


class SocialMedia(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='social_media/', validators=[
        FileExtensionValidator(
            allowed_extensions=['jpg', 'jpeg', 'png', 'svg', 'webp', 'JPG', 'JPEG', 'PNG', 'SVG', 'WEBP']),
        check_image_size], blank=True,
                              null=True)
    link = models.URLField()

    def __str__(self):
        return self.name


class Location(models.Model):
    country = models.CharField(max_length=100, null=True, blank=True)
    region = models.CharField(max_length=100, null=True, blank=True)
    district = models.CharField(max_length=100, null=True, blank=True)
    street = models.CharField(max_length=255, null=True, blank=True)
    house = models.CharField(max_length=50, null=True, blank=True)
    postalCode = models.CharField(max_length=20, null=True, blank=True)
    fullAddress = models.TextField(null=True, blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f"{self.country}, {self.region}, {self.district}"


class PhoneNumber(models.Model):
    number = models.JSONField(max_length=100)

    def __str__(self):
        return self.number


class Email(models.Model):
    email = models.JSONField()

    def __str__(self):
        return self.email


class WorkTime(models.Model):
    work_time = models.CharField()

    def __str__(self):
        return self.work_time
