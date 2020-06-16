from django.db import models

from autoslug import AutoSlugField
from model_utils.models import TimeStampedModel


class Post(TimeStampedModel):
    name = models.CharField("Name of Cheese", max_length=255)
    slug = AutoSlugField("Cheese Address",
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

    def __str__(self):
        return self.name

