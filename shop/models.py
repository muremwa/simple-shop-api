from django.db import models
from django.utils.text import slugify


class ProductCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(blank=True, unique=True)
    objects = models.Manager()

    class Meta:
        verbose_name_plural = 'Product categories'

    def save(self, *args, **kwargs):
        # save first in order to get the pk
        super().save()

        # add the pk to the slug url
        self.slug = slugify(str(self.name) + "-" + str(self.pk))
        super().save()

    def __str__(self):
        return self.name
