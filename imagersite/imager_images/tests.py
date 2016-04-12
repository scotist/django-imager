"""Test photo and album models."""
from django.db.models.fields.files import ImageFieldFile
from django.test import TestCase, override_settings
from django.utils import timezone
from .models import Photo, Album, PUBLISHED_CHOICES
from imager_profile.tests import UserFactory
import factory
import random

PHOTO_BATCH_SIZE = 20
ALBUM_BATCH_SIZE = 10
USER_BATCH_SIZE = 5


class PhotoFactory(factory.django.DjangoModelFactory):
    """Create testing model of photo."""

    class Meta:
        """Make photo model factory product."""

        model = Photo

    title = factory.Faker('sentence')
    description = factory.Faker('text')
    published = random.choice(PUBLISHED_CHOICES)
    owner = factory.SubFactory(UserFactory, username='AlphaUser')
    img_file = factory.django.ImageField()


class AlbumFactory(factory.django.DjangoModelFactory):
    """Create testing model of album."""

    class Meta:
        """Make album model factory product."""

        model = Album

    title = factory.Faker('sentence')
    description = factory.Faker('text')
    published = random.choice(PUBLISHED_CHOICES)
    owner = factory.SubFactory(UserFactory, username='AlphaUser')


class SinglePhotoOrAlbum(object):
    """Test singles instance of an album or photo."""

    def test_exists(self):
        """Test factory product exists."""
        self.assertTrue(self.instance)
