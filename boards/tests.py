from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User
from .views import new_topic
from .models import Board, Topic, Post


class BoardsTests(TestCase):

    def test_boards_view(self):
        """ Test boards view status code and that
        the correct view funciton is returned """
        url = reverse('boards')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'boards/boards.html')


class BoardTopicsTests(TestCase):
    # ...

    def test_board_topics_view_contains_navigation_links(self):
        board_topics_url = reverse('board_topics', kwargs={'pk': 1})
        homepage_url = reverse('boards')
        new_topic_url = reverse('new_topic', kwargs={'pk': 1})

        response = self.client.get(board_topics_url)

        self.assertContains(response, 'href="{0}"'.format(homepage_url))
        self.assertContains(response, 'href="{0}"'.format(new_topic_url))


class NewTopicTests(TestCase):

    def setUp(self):
        Board.objects.create(name='Test', description='Test board.')
        User.objects.create_user(username='john', email='john@doe.com', password='123')  # <- included this line here

    def test_csrf(self):
        url = reverse('new_topic', kwargs={'pk': 1})
        response = self.client.get(url, follow=True)
        self.assertContains(response, 'csrfmiddlewaretoken')