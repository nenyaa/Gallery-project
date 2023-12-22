from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Gallery, Picture


# Create your views here.
class GalleryList(ListView):
    model = Gallery
    paginate_by = 10


class GalleryDetail(DetailView):
    model = Gallery


class PictureDetail(DetailView):
    model = Picture

    def get_queryset(self):
        picture_pk = self.kwargs['picture_pk']
        objects = Picture.objects.filter(pk=picture_pk)
        return objects
