from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.render_blog_homepage, name='homepage_url'),

]
