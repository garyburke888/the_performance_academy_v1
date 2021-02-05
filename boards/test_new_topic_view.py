from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import resolve, reverse

from .forms import NewTopicForm
from .models import Board, Post, Topic
from .views import new_topic


class LoginRequiredNewTopicTests(TestCase):
    def setUp(self):
        """ Create a test board """
        Board.objects.create(name='Test', description='Test board.')
        self.url = reverse('new_topic', kwargs={'pk': 1})
        self.response = self.client.get(self.url)

    def test_redirection(self):
        """ Test user is redirected to the sites login page """
        login_url = reverse('account_login')
        self.assertRedirects(
            self.response, '{login_url}?next={url}'.format(
                login_url=login_url, url=self.url))


class NewTopicTests(TestCase):
    def setUp(self):
        """ Create test board with test user """
        Board.objects.create(name='Test', description='Test board.')
        User.objects.create_user(
            username='test', email='test@test.com', password='123456')
        self.client.login(username='test', password='123456')

    def test_new_topic_view_success_status_code(self):
        """ Test topic view status code """
        url = reverse('new_topic', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_new_topic_view_not_found_status_code(self):
        """ Test status code for a topic that doesn't exist
        returns a 404 error """
        url = reverse('new_topic', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_new_topic_url_resolves_new_topic_view(self):
        """ Test topic url resolves to correct view """
        view = resolve('/boards/1/new/')
        self.assertEquals(view.func, new_topic)
