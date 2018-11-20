from django.shortcuts import render
from django.views.generic.list import ListView
import django_tables2 as tables

from datasets.models import Dataset
from datasets.tables import DatasetTable


def index(request):
    context = {}
    return render(request, 'datasets/index.html', context)


class DatasetListView(tables.SingleTableView):
    table_class = DatasetTable
    queryset = Dataset.objects.filter(sharing=True)
    template_name = 'datasets/datasets_list.html'
