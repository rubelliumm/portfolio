from django.urls import path
from jobapp import views

app_name = "jobapp"
urlpatterns = [
    path("", views.renderJobappHomePage, name="jobapp_homepage_url"),
    path("allcircular/", views.renderAllCircularPage, name="all_circular_page_url"),
    path(
        "circular/<int:cid>",
        views.renderCircularDetailsPage,
        name="individual_circular_page_url",
    ),
    path("save/<int:cid>", views.saveCircular, name="save_circular_url"),
    path("unsave/<int:cid>", views.unSaveCircular, name="unsave_circular_url"),
    path(
        "iscircularsaved/<int:cid>", views.isCircularSaved, name="is_circular_saved_url"
    ),
    path(
        "savedcircular/",
        views.viewSavedCircular,
        name="saved_circular_page_url",
    ),
    path("topics/", views.renderTopicsPage, name="topics_page_url"),
]
