from django.urls import reverse, resolve
from django.test import TestCase

from datasets.views import index


class DatasetIndexViewTests(TestCase):
    def test_index_view_is_available(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_index_url_resolves_index_view(self):
        view = resolve('/')
        self.assertEquals(view.func, index)
