from collections.abc import Iterable
from django.db import models


# Create your models here.
class TimestampedModel(models.Model):
    modified_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Gallery(TimestampedModel):
    title = models.CharField(max_length=200)

    def __str__(self): return self.title


class Picture(TimestampedModel):
    img = models.ImageField(upload_to="gallery/%Y/%m/%d")
    text = models.CharField(max_length=200)
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)

    def __str__(self): return self.text

    def save(self, force_insert: bool = ..., force_update: bool = ..., using: str | None = ...,
             update_fields: Iterable[str] | None = ...) -> None:
        super().save(force_insert, force_update, using, update_fields)
