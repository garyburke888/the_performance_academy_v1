from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Article

# Create your tests here.


class TestModels(TestCase):

    def test_title_field_cannot_be_empty(self):
        """ Raise validation error it title field
        is left blank """
        article = Article(
            title='',
            body='here is some text',
            date='2021-01-01',
            image='noimage2.png'
        )
        article.full_clean()
        self.assertRaises(ValidationError, article.full_clean)

    def test_string_representation(self):
        """ Ensure that a blog entry’s string
        representation is equal to its title """
        entry = Article(title="My entry title")
        self.assertEqual(str(entry), entry.title)
