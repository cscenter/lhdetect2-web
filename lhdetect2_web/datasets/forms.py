from django import forms
from datasets.models import Dataset, Image


class DatasetForm(forms.ModelForm):
    class Meta:
        model = Dataset
        exclude = ['user', 'images', 'custom_fields']


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('file', )
