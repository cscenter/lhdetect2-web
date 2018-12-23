from django.db import models
from django.contrib.postgres.fields import JSONField
from enum import Enum
from sorl.thumbnail import ImageField

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


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class Image(models.Model):
    title = models.CharField(max_length=255, blank=True)
    file = ImageField(upload_to='images/')
    date_uploaded = models.DateTimeField(auto_now_add=True)
    lhdetect_desc = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


class Dataset(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=50)
    sharing = models.CharField(max_length=7,
                               choices=[(member.name, member.value) for member in SharingMode],
                               default=SharingMode.PUBLIC.name)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    separator = models.CharField(max_length=5, default='_')
    images = models.ManyToManyField(Image)

    parent1 = models.CharField(max_length=200, null=True, blank=True)
    parent2 = models.CharField(max_length=200, null=True, blank=True)
    gen_type = models.CharField(max_length=10, verbose_name="Generation Type",
                                choices=[(member.name, member.value) for member in GenerationType], blank=True)
    generation = models.PositiveSmallIntegerField(null=True, blank=True)

    place = models.CharField(max_length=13,
                             choices=[(member.name, member.value) for member in GrowthFacility], blank=True)
    watering = models.CharField(max_length=8,
                                choices=[(member.name, member.value) for member in Watering], blank=True)

    repetition = models.PositiveIntegerField(null=True, blank=True)
    # TODO: restrict to month and year only
    vegetation_date = models.DateField(null=True, blank=True)

    custom_fields = JSONField(null=True)

    def __str__(self):
        return self.title
