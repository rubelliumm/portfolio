from django.urls import path
from myserver import views

urlpatterns = [
    path('', views.server_home, name='server_homepage_url'),
]
