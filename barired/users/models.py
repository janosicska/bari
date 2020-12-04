from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Contact(models.Model):
    user_from = models.ForeignKey('User', related_name='rel_from_set', on_delete=models.CASCADE)
    user_to = models.ForeignKey('User', related_name='rel_to_set', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.user_from} follows {self.user_to}'


class User(AbstractUser):
    name = models.CharField(
        _("Name of User"), blank=True, max_length=255
    )
    bio = models.TextField("Bio", blank=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    following = models.ManyToManyField('self', through=Contact, related_name='followers', symmetrical=False)

    def get_absolute_url(self):
        return reverse(
            "users:detail", kwargs={"username": self.username}
        )



