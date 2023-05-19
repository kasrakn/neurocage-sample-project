from django.contrib import admin
from django.urls import path, include
from webApp.views import CageListView

urlpatterns = [
    path('', CageListView.as_view(), name='cage-list'),
    # path('add_stager', AddStagerView.as_view(), name='add_stager'),
]