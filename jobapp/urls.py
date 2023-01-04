from django.urls import path
from jobapp import views

app_name = 'jobapp'
urlpatterns = [
    path('', views.render_jobapp_home, name='jobapp_homepage_url'),
]
