from django.shortcuts import render
from django.views import View
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


class UserDatasetListView(tables.SingleTableView):
    table_class = DatasetTable
    template_name = 'datasets/datasets_list.html'

    def get_queryset(self):
        return Dataset.objects.filter(user_id=self.request.user.id)

    def get_context_data(self, **kwargs):
        context = super(UserDatasetListView, self).get_context_data()
        context['list_name'] = 'My Datasets'
        return context


class PublicDatasetListView(tables.SingleTableView):
    table_class = DatasetTable
    queryset = Dataset.objects.filter(sharing=SharingMode.PUBLIC.name)
    template_name = 'datasets/datasets_list.html'

    def get_context_data(self, **kwargs):
        context = super(PublicDatasetListView, self).get_context_data()
        context['list_name'] = 'Public Datasets'
        return context


def upload_image(request):
    form = ImageForm(request.POST, request.FILES)
    if form.is_valid():
        image = form.save()
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