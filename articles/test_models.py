from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Article

# Create your tests here.


class TestModels(TestCase):

    def test_title_field_cannot_be_empty(self):
        article = Article(
            title='',
            body='here is some text',
            date='2021-01-01',
            image='noimage2.png'
        )
        article.full_clean()
        self.assertRaises(ValidationError, article.full_clean)
