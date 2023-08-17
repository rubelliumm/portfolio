from django.urls import path
from customAdmin import views

app_name = "customAdmin"

urlpatterns = [
    path("", views.admin_home, name="homepage_url"),
]
