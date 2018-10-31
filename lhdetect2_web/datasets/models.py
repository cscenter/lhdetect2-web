from django.db import models
from django.contrib.postgres.fields import JSONField
from enum import Enum
from lhdetect2_web.users.models import CustomUser


class Dataset(models.Model):
    class GenerationType(Enum):
        UNKNOWN = 'undefined'
        CLEAN_LINE = 'clean line'
        HYBRID = 'hybrid'

    class GrowthFacility(Enum):
        UNKNOWN = 'undefined'
        FIELD = 'field'
        GREENHOUSE = 'greenhouse'
        PLANT_CHAMBER = 'plant chamber'

    class Watering(Enum):
        UNKNOWN = 'undefined'
        WATERING = 'watering'
        DROUGHT = 'drought'

    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=50)
    sharing = models.BooleanField(default=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    separator = models.CharField(max_length=5, default='_')
    files_path = models.FilePathField(path="", allow_files=False, allow_folders=True)

    parent1 = models.CharField(max_length=200)
    parent2 = models.CharField(max_length=200)
    gen_type = models.CharField(max_length=10,
                                choices=[(tag, tag.value) for tag in GenerationType])
    generation = models.PositiveSmallIntegerField()

    place = models.CharField(max_length=13,
                             choices=[(tag, tag.value) for tag in GrowthFacility])
    watering = models.CharField(max_length=8,
                                choices=[(tag, tag.value) for tag in Watering])

    repetition = models.PositiveIntegerField()
    # TODO: restrict to month and year only
    vegetation_date = models.DateField()

    custom_fields = JSONField()



