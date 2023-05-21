from django.contrib import admin
from django.urls import path, include
from webApp.views import CageListView, CageCreateView, CageDetailView, UpdateCageView, DeleteCageView

urlpatterns = [
    path('', CageListView.as_view(), name='cage-list'),
    path('cage/add', CageCreateView.as_view(), name='add-cage'),
    path('cage/<int:pk>', CageDetailView.as_view(), name='cage-detail'),
    path('cage/edit/<int:pk>', UpdateCageView.as_view(), name="edit-cage"),
    path('cage/<int:pk>/delete', DeleteCageView.as_view(), name="delete-cage"),
]