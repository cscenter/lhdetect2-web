from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.template.loader import render_to_string
import django_tables2 as tables

from datasets.models import Dataset
from datasets.tables import DatasetTable
from datasets.forms import DatasetForm


def index(request):
    context = {}
    return render(request, 'datasets/index.html', context)


def create_dataset(request):
    form = DatasetForm()
    context = {
        'form': form
    }
    html_form = render_to_string('datasets/includes/partial_dataset_create.html',
                                 context, request=request)

    return JsonResponse({
        'html_form': html_form
    })


class DatasetListView(tables.SingleTableView):
    table_class = DatasetTable
    queryset = Dataset.objects.filter(sharing=True)
    template_name = 'datasets/datasets_list.html'


class ImageUploadView(View):
    def get(self):
        pass
