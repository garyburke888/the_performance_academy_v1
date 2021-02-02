from django.test import TestCase
from .forms import ArticleForm


class TestArticleForm(TestCase):

    def test_item_title__is_required(self):
        form = ArticleForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = ArticleForm()
        self.assertEqual(form.Meta.fields, '__all__')
