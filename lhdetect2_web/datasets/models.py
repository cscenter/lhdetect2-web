from django.db import models
from django.contrib.postgres.fields import JSONField
from enum import Enum
from users.models import CustomUser


class SharingMode(Enum):
    PRIVATE = 'private'
    PUBLIC = 'public'


class GenerationType(Enum):
    CLEAN_LINE = 'clean line'
    HYBRID = 'hybrid'


class GrowthFacility(Enum):
    FIELD = 'field'
    GREENHOUSE = 'greenhouse'
    PLANT_CHAMBER = 'plant chamber'


class Watering(Enum):
    WATERING = 'watering'
    DROUGHT = 'drought'


class Image(models.Model):
    title = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='images/')
    date_uploaded = models.DateTimeField(auto_now_add=True)


class Dataset(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=50)
    sharing = models.CharField(max_length=7,
                               choices=[(member.name, member.value) for member in SharingMode],
                               default=SharingMode.PUBLIC)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    separator = models.CharField(max_length=5, default='_')
    files_path = models.FilePathField(path="", allow_files=False, allow_folders=True, blank=True)

    parent1 = models.CharField(max_length=200)
    parent2 = models.CharField(max_length=200)
    gen_type = models.CharField(max_length=10,
                                choices=[(member.name, member.value) for member in GenerationType], blank=True)
    generation = models.PositiveSmallIntegerField()

    place = models.CharField(max_length=13,
                             choices=[(member.name, member.value) for member in GrowthFacility], blank=True)
    watering = models.CharField(max_length=8,
                                choices=[(member.name, member.value) for member in Watering], blank=True)

    repetition = models.PositiveIntegerField()
    # TODO: restrict to month and year only
    vegetation_date = models.DateField()

    custom_fields = JSONField()

