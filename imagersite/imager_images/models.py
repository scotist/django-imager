"""Model phots and albums for database items."""

from django.db import models
from django.conf import settings

# Create your models here.

PUBLISHED_CHOICES = ['private', 'shared', 'public']
PUBLISHED_DEFAULT = PUBLISHED_CHOICES[0]


class Photo(models.Model):
    """Model a single photo in database."""

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='photos')
    albums = models.ManyToManyField('Album', related_name='photos')
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_uploaded = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(auto_now_add=True)
    published = models.CharField(max_length=255,
                                 choices=PUBLISHED_CHOICES,
                                 default=PUBLISHED_DEFAULT)

    def __str__(self):
        """Sting output for photo item."""
        return "{}... ({})".format(
            self.title[:20],
            self.date_published)


class Album(models.Model):
    """Model a photo album collection in database."""

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='albums')
    cover = models.ForeignKey('Photo',
                              related_name='covered_albums',
                              null=True,
                              default=None)
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(auto_now_add=True)
    published = models.CharField(max_length=255,
                                 choices=PUBLISHED_CHOICES,
                                 default=PUBLISHED_DEFAULT)

    def set_cover(self, photo):
        """Set cover photo for album."""
        if photo.owner != self.owner:
            raise ValueError('{} does not have permission to use {}.'.format(
                self.owner, photo))
        if photo not in self.photos.all():
            raise KeyError('{} is not here!'.format(photo))

        self.cover = photo
        self.save()

    def _allowed_photos(self, photos):
        """Generate list of owner's photos that can be put in album."""
        for photo in photos:
            if photo.owner is self.owner:
                yield photo

    def add_photos(self, photos):
        """Add owner's photos to album."""
        for photo in self._allowed_photos(photos):
            photo.albums.add(self)
            photo.save()
            if self.cover is None:
                self.set_cover(photo)
