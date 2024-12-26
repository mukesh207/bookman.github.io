from django.db import models

# Create your models here.
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField()
    isbn_number = models.CharField(max_length=13)
    page_count = models.IntegerField()
    cover_image = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
