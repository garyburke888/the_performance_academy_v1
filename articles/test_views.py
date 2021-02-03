from django.test import TestCase

# Create your tests here.


class TestViews(TestCase):

    def test_get_article_list_view(self):
        response = self.client.get('/articles/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'articles/blog.html')

    def test_get_add_article_view(self):
        response = self.client.get('/articles/add/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, '/accounts/login/?next=/articles/add/')

    def test_edit_article_view(self):
        response = self.client.get('/articles/edit/3')
        self.assertEqual(response.status_code, 301)
