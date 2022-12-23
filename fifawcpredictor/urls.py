from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='fifa_home_page_url'),
]
