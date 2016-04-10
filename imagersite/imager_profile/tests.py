# Create your tests here.

from __future__ import unicode_literals
from django.test import TestCase
from django.contrib.auth.models import User
import factory


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User


class UserTestCase(TestCase):

    def setUp(self):
        self.user = UserFactory.create(
            username='bob',
            email='bob@bobertson.com',
        )
        self.user.set_password('secret')

    def test_foo(self):
        import pdb; pdb.set_trace()