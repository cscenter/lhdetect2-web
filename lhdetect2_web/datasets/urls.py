from django.urls import path

from datasets import views

app_name = 'datasets'

urlpatterns = [
    path('', views.index, name='index'),
    path('public/', views.public_datasets, name='public'),
    path('user/', views.user_datasets, name='user'),
    path('create/', views.create_dataset, name='create_dataset'),
    path('upload/', views.upload_image, name='upload_image'),
    path('<int:id>/', views.dataset_images, name='dataset_images'),
    path('<int:id>/delete/', views.delete_dataset, name='delete_dataset')
]
