"""User Profile Models."""
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ImagerProfile(models.Model):
    """Class defining imager profile model."""

    user = models.OneToOneField(User, related_name='profile', null=False)
    camera_model = models.CharField(max_length=250)
    photography_genre = models.TextField()
    contacts = models.ManyToManyField('self')
    address = models.TextField()
    website = models.URLField()


class ActiveProfileManager(models.Manager):
    """Model manager limited to active profiles."""

    def get_queryset(self):
        """Filter queryset to get default users."""
        queryset = super(ActiveProfileManager, self).get_queryset()
        return queryset.filter(user__is_active=True)

objects = models.Manager()
active = ActiveProfileManager()


def is_active(self):
    """Indicate when a user is active."""
    return self.user.is_active
