"""User Profile Models."""
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.


class ActiveProfileManager(models.Manager):
    """Model manager limited to active profiles."""

    def get_queryset(self):
        """Filter queryset to get default users."""
        queryset = super(ActiveProfileManager, self).get_queryset()
        return queryset.filter(user__is_active=True)


class ImagerProfile(models.Model):
    """Class defining imager profile model."""

    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='profile', null=False)
    camera_model = models.CharField(max_length=250)
    photography_genre = models.TextField(default='')
    contacts = models.ManyToManyField('self', default='')
    address = models.TextField(default='')
    website = models.URLField(default='')
    active = ActiveProfileManager()

    def __str__(self):
        """String output for imager profile model."""
        return "Imager profile for user: {}".format(self.user.username)

    @property
    def is_active(self):
        """Indicate when a user is active."""
        return self.user.is_active


# objects = models.Manager()

# active = ActiveProfileManager()


