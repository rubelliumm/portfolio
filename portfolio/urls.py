from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path(
        "admin/",
        admin.site.urls,
    ),
    path("custom-admin/", include("customAdmin.urls")),
    path("", include("main.urls")),
    path("fifawcpredictor/", include("fifawcpredictor.urls")),
    path("todo/", include("todo.urls")),
    path("blog/", include("blog.urls")),
    path("image-to-text/", include("imageToTextConverter.urls")),
    path("server/", include("myserver.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
