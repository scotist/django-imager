"""Test ImagerProfile model."""

# Create your tests here.

from __future__ import unicode_literals
from django.test import TestCase
from django.conf import settings
from django.db.models import QuerySet, Manager
from .models import ImagerProfile
import random
from django.contrib.auth.models import User
import factory

USER_BATCH_SIZE = 50


class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = settings.AUTH_USER_MODEL
        django_get_or_create = ('username',)

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')
    username = factory.LazyAttribute(
        lambda obj: ''.join((obj.first_name, obj.last_name)))
    password = factory.PostGenerationMethodCall('set_password',
                                                'secret')


class SingleUserCase(TestCase):

    def setUp(self):
        self.user = UserFactory.create()


class UserCase(SingleUserCase):
    """Test case for photos."""

    def test_profile_exists(self):
        """Test that user has profile."""
        self.assertTrue(self.user.profile)

    def test_profile_active(self):
        """Test inactive profile."""
        self.assertTrue(self.user.profile.is_active)
