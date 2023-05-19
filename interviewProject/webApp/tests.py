from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve, reverse_lazy
from webApp.views import CageListView

# Create your tests here.

class TestUrls(SimpleTestCase):

    def test_cage_list_url(self):
        url = reverse('cage-list')
        self.assertEqual(resolve(url).func.view_class, CageListView)