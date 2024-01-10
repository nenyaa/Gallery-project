
from django.urls import path
from . import views

app_name = "gallery"
urlpatterns = [
    path("", views.GalleryList.as_view(), name="list"),
    path("<int:pk>", views.GalleryDetail.as_view(), name="details"),
    path("<int:pk>/images/<int:picture_pk>", views.PictureDetail.as_view(), name="picture-details")
    ]
