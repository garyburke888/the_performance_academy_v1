from django.test import TestCase
from django.urls import resolve, reverse
from .models import Board
from .views import BoardListView


class BoardsTests(TestCase):

    def setUp(self):
        """ Create a new test board """
        self.board = Board.objects.create(
            name='Django', description='Django board.')
        url = reverse('boards')
        self.response = self.client.get(url)

    def test_boards_view_status_code(self):
        """ Test the boards view status code """
        self.assertEquals(self.response.status_code, 200)

    def test_boards_url_resolves_boards_view(self):
        """ Test the boards url resolves to correct view """
        view = resolve('/boards/')
        self.assertEquals(view.func.view_class, BoardListView)

    def test_boards_view_contains_link_to_topics_page(self):
        """ Test the boards view links to its topic page """
        board_topics_url = reverse(
            'board_topics', kwargs={'pk': self.board.pk})
        self.assertContains(
            self.response, 'href="{0}"'.format(board_topics_url))
