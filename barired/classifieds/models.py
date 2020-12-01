from django.db import models
from django.urls import reverse
from django.conf import settings

from autoslug import AutoSlugField


class Classified(models.Model):
    CATEGORIES = [
        (None, 'Select the category'),
        ('RealEstate', 'Real Estate'),
        ('Cars', 'Cars'),
        ('Clothing', 'Clothing'),
        ('Furniture', 'Furniture'),
        ('Technology', 'Technology'),
        ('Services', 'Services'),
    ]
    title = models.CharField("Title", max_length=255)
    slug = AutoSlugField("Classified Address", unique=True, always_update=False, populate_from="title")
    photo = models.ImageField(upload_to='classifieds/%Y/%m/%d/', blank=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    category = models.CharField(choices=CATEGORIES, max_length=20, null=True)
    description = models.TextField("Description", blank=True)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.SET_NULL
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Return absolute URL to the Post Detail page."""
        return reverse('classifieds:classified_detail', args=[self.id, self.slug])
