import uuid

from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)


class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=1024)
    whole_pages = models.DecimalField(max_digits=5, decimal_places=0)
    read_pages = models.DecimalField(max_digits=5, decimal_places=0)
    progress = models.FloatField()
    pid = models.CharField(max_length=25, default=uuid.uuid4(), unique=True)

    def save(self, *args, **kwargs):
        self.progress = (self.read_pages / self.whole_pages) * 100
        super(Book, self).save(*args, **kwargs)

    class Meta:
        indexes = [models.Index(fields=["title", "pid"])]
