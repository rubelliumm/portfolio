from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('custom-admin/', include('customAdmin.urls')),
    path('', include('main.urls')),
    path('fifawcpredictor/', include('fifawcpredictor.urls')),
    path('todo/', include('todo.urls')),
    path('jobapp/', include('jobapp.urls')),
    path('blog/', include('blog.urls')),

]
