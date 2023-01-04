from django.urls import path
from . import views

app_name = 'imageToTextConverter'
urlpatterns = [
    path('', views.upload_file, name='converter_homepage_url'),
]
