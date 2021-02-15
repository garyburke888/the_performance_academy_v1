from django.test import TestCase
from .models import Article

# Create your tests here.


class TestModels(TestCase):

    def test_string_representation(self):
        """ Ensure that a blog entry’s string
        representation is equal to its title """
        entry = Article(title="My entry title")
        self.assertEqual(str(entry), entry.title)
