from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=128, db_index=True)
    slug = models.SlugField(max_length=128, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=128)
    category = models.ForeignKey(Category, related_name='Products', on_delete=models.CASCADE())
