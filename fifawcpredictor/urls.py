from django.urls import path
from . import views

app_name = 'fifawcpredictor'

urlpatterns = [
    path('', views.home, name='fifa_home_page_url'),
]
