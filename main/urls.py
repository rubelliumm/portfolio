from django.urls import path
from . import views

urlpatterns = [
    path('', views.render_index_page, name='index_page_url'),
    path('about/', views.render_about_page, name='about_page_url'),
    path('contact/', views.render_contact_page, name='contact_page_url'),
    path('services/', views.render_services_page, name='service_page_url'),
    path('allprojects/', views.render_allprojects_page,
         name='allprojects_page_url'),
    path('applist/', views.render_applist_page, name='applist_page_url'),
    path('sign-up/', views.registration, name='registration_page_url'),
    path('sign-in/', views.userLogin, name='login_page_url')
]
