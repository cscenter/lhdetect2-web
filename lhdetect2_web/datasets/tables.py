import django_tables2 as tables

from datasets.models import Dataset


class DatasetTable(tables.Table):
    class Meta:
        model = Dataset
        fields = ('title', 'date_updated', 'user')
