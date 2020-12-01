from django.db import models
from django.urls import reverse
from django.conf import settings

from autoslug import AutoSlugField
from model_utils.models import TimeStampedModel


class Post(models.Model):
    name = models.CharField("Title", max_length=255)
    slug = AutoSlugField("Post Address",
                         unique=True, always_update=False, populate_from="name")
    photo = models.ImageField(upload_to='posts/%Y/%m/%d/', blank=True)
    description = models.TextField("Description", blank=True)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.SET_NULL
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Return absolute URL to the Post Detail page."""
        return reverse('posts:post_detail',
                       args=[self.id, self.slug])


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.SET_NULL
    )
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'
