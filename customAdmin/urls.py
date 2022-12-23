from django.urls import path
from customAdmin import views

urlpatterns = [
    path('', views.admin_home, name='admin_home'),
]
