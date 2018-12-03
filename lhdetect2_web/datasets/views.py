from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.template.loader import render_to_string
import django_tables2 as tables

from datasets.models import Dataset
from datasets.tables import DatasetTable
from datasets.forms import DatasetForm, ImageForm


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


def upload_image(request):
    form = ImageForm(request.POST, request.FILES)
    if form.is_valid():
        image = form.save()
        data = {
            'is_valid': True,
            'name': image.file.name,
            'url': image.file.url
        }
    else:
        data = {
            'is_valid': False
        }

    return JsonResponse(data)