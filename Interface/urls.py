from django.urls import path
from . import views  

urlpatterns = [
    path('', views.file_upload_view, name='file-upload'),
]