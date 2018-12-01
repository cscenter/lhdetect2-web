from django import forms
from datasets.models import Dataset, Image


class DatasetForm(forms.ModelForm):
    class Meta:
        model = Dataset
        fields = ('title', 'sharing', )


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('file', )
