from django.db import models
from django.urls import reverse
from django.conf import settings

from autoslug import AutoSlugField
from model_utils.models import TimeStampedModel


class Post(TimeStampedModel):
    name = models.CharField("Title", max_length=255)
    slug = AutoSlugField("Post Address",
                         unique=True, always_update=False, populate_from="name")
    description = models.TextField("Description", blank=True)

    class Type(models.TextChoices):
        UNSPECIFIED = "unspecified", "Unspecified"
        Social = "social", "Social"
        Eventos = "eventos", "Eventos"
        Cultura = "cultura", "Cultura"
        HARD = "clasificados", "Clasificados"

    type = models.CharField("Type", max_length=20,
                                choices=Type.choices, default=Type.UNSPECIFIED)

    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Return absolute URL to the Post Detail page."""
        return reverse(
            'posts:detail', kwargs={"slug": self.slug}
        )
