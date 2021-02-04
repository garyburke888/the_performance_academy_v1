from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Article

# Create your tests here.


class TestModels(TestCase):

    def test_author_field_must_be_user_instance(self):
        article = Article()
        article.title = 'hello'
        self.assertRaises(ValidationError)
