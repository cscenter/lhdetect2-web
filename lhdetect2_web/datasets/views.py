from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.http import JsonResponse
from django.template.loader import render_to_string
import django_tables2 as tables

from datasets.models import Dataset, SharingMode, Image
from datasets.tables import DatasetTable
from datasets.forms import DatasetForm, ImageForm
from users.models import CustomUser


def index(request):
    context = {}
    return render(request, 'datasets/index.html', context)


def create_dataset(request):
    data = dict()

    if request.method == 'POST':
        form = DatasetForm(request.POST)
        if form.is_valid():
            dataset = form.save(commit=False)
            dataset.user = CustomUser.objects.get(id=request.user.id)
            dataset.save()

            form_data = request.POST.copy()
            image_ids = form_data.get("images").split(',')
            images = Image.objects.filter(id__in=image_ids)
            dataset.images.add(*images)

            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    else:
        form = DatasetForm()

    context = {
        'form': form
    }
    data['html_form'] = render_to_string('datasets/includes/partial_dataset_create.html',
                                         context, request=request)

    return JsonResponse(data)


def user_datasets(request):
    datasets = Dataset.objects.filter(user_id=request.user.id)

    context = {
        'datasets': datasets,
        'list_name': 'My Datasets'
    }

    return render(request, 'datasets/datasets_list.html', context)


def public_datasets(request):
    datasets = Dataset.objects.filter(sharing=SharingMode.PUBLIC.name)

    context = {
        'datasets': datasets,
        'list_name': 'Public Datasets'
    }

    return render(request, 'datasets/datasets_list.html', context)


def dataset_images(request, id):
    dataset = get_object_or_404(Dataset, id=id)
    images = dataset.images.order_by('title')

    context = {
        'dataset': dataset,
        'images': images
    }

    return render(request, 'datasets/dataset_images.html', context)


def upload_image(request):
    form = ImageForm(request.POST, request.FILES)
    if form.is_valid():
        image = form.save(commit=False)
        image.title = image.file.name
        image.save()

        data = {
            'is_valid': True,
            'name': image.file.name,
            'url': image.file.url,
            'id': image.pk
        }
    else:
        data = {
            'is_valid': False
        }

    return JsonResponse(data)