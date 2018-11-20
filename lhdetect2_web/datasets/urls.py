from django.urls import path

from datasets import views

urlpatterns = [
    path('', views.index, name='index'),
    path('public/', views.DatasetListView.as_view(), name='public')
]
