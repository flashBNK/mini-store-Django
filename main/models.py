from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=128, db_index=True)
    slug = models.SlugField(max_length=128, unique=True)

    class Meta:
        ordering = ('name',)

