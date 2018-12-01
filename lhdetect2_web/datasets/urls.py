from django.urls import path

from datasets import views

urlpatterns = [
    path('', views.index, name='index'),
    path('public/', views.DatasetListView.as_view(), name='public'),
    path('create/', views.create_dataset, name='create_dataset')
    # path('upload/', views.BasicUploadView.as_view(), name='upload')
]
