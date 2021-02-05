from django.test import TestCase
from django.urls import resolve, reverse

from .models import Board
from .views import TopicListView


class BoardTopicsTests(TestCase):
    def setUp(self):
        """ Creat a new test topic """
        Board.objects.create(name='Django', description='Django board.')

    def test_board_topics_view_success_status_code(self):
        """ Test the topics view status code """
        url = reverse('board_topics', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_board_topics_view_not_found_status_code(self):
        """ Test status code for a topic that doesn't exist
        returns a 404 error """
        url = reverse('board_topics', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_board_topics_url_resolves_board_topics_view(self):
        """ Test the topics url resolves to the correct view """
        view = resolve('/boards/1/')
        self.assertEquals(view.func.view_class, TopicListView)

    def test_board_topics_view_contains_navigation_links(self):
        """ Test tpoics page contains links to boards page and
        to add a new topic (page) """
        board_topics_url = reverse('board_topics', kwargs={'pk': 1})
        homepage_url = reverse('boards')
        new_topic_url = reverse('new_topic', kwargs={'pk': 1})
        response = self.client.get(board_topics_url)
        self.assertContains(response, 'href="{0}"'.format(homepage_url))
        self.assertContains(response, 'href="{0}"'.format(new_topic_url))
