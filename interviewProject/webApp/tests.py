from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse, resolve, reverse_lazy
from webApp.views import CageListView
from datetime import datetime, timedelta

from webApp.forms import CreateCageForm
from webApp.models import Cage, SensorData
# Create your tests here.

class TestUrls(SimpleTestCase):

    def test_cage_list_url(self):
        url = reverse('cage-list')
        self.assertEqual(resolve(url).func.view_class, CageListView)


class TestModels(TestCase):
    
    def test_cage_latest_health_status(self):
        cage1 = Cage.objects.create(label='c1')

        SensorData.objects.create(
            cage=cage1,
            health_status=2,
            is_successful=True,
            timestamp=datetime.now()
        )
        SensorData.objects.create(
            cage=cage1,
            health_status=None,
            is_successful=False,
            timestamp=datetime.now() + timedelta(minutes=2)
        )

        self.assertEqual(cage1.latest_health_status, 2)

    

class TestForms(TestCase):

    def test_create_cage_form_valid_data(self):
        form = CreateCageForm(data={
            'label':"test label"
        })
        self.assertTrue(form.is_valid())

    
    def test_create_cage_form_invalid_data(self):
        form = CreateCageForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()


    def test_cage_list_view_GET(self):
        url = reverse('cage-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


    def test_create_cage_view_GET(self):
        url = reverse('add-cage')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add-cage.html')

    
    def test_create_cage_view_POST_adds_new_cage(self):
        url = reverse('add-cage')
        cage_label = 'test cage label'
        response = self.client.post(url, data={
            'label': cage_label
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Cage.objects.last().label, cage_label)
    
    
    def test_create_cage_view_POST_no_data(self):
        url = reverse('add-cage')
        response = self.client.post(url, data={})

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('edit-cage.html')
        self.assertEqual(Cage.objects.count(), 0)

    
    def test_cage_detail_view_GET(self):
        cage1 = Cage.objects.create(label="cage1 label")
        self.create_cage_url = reverse('cage-detail', args=[cage1.pk])
        url = reverse('cage-detail', args=[cage1.pk])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('cage-detail.html')

    
    def test_update_cage_view_GET(self):
        cage1 = Cage.objects.create(label="cage1 label")
        self.create_cage_url = reverse('cage-detail', args=[cage1.pk])
        url = reverse('edit-cage', args=[cage1.pk])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit-cage.html')

    
    def test_update_cage_view_POST_adds_new_cage(self):
        cage1 = Cage.objects.create(label="cage1 label")
        self.create_cage_url = reverse('cage-detail', args=[cage1.pk])
        url = reverse('edit-cage', args=[cage1.pk])
        cage_label = 'test cage label'
        response = self.client.post(url, data={
            'label': cage_label
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Cage.objects.last().label, cage_label)
    
    
    def test_update_cage_view_POST_no_data(self):
        cage1 = Cage.objects.create(label="cage1 label")
        self.create_cage_url = reverse('cage-detail', args=[cage1.pk])
        url = reverse('edit-cage', args=[cage1.pk])
        response = self.client.post(url, data={})

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('edit-cage.html')

    
    def test_cage_delete_GET(self):
        cage1 = Cage.objects.create(label="cage1 label")
        self.create_cage_url = reverse('cage-detail', args=[cage1.pk])
        url = reverse('delete-cage', args=[cage1.pk])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('delete-cage')

    
    def test_cage_delete_POST_with_data(self):
        cage1 = Cage.objects.create(label="cage1 label")
        self.create_cage_url = reverse('cage-detail', args=[cage1.pk])
        new_label = 'cage test label'

        url = reverse('delete-cage', args=[cage1.pk])
        response = self.client.post(url, data={
            'label': new_label
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Cage.objects.count(), 0)