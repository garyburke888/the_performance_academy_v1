from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import resolve, reverse

from .forms import PostForm
from .models import Board, Post, Topic
from .views import reply_topic


class ReplyTopicTestCase(TestCase):
    '''
    Base test case to be used in all `reply_topic` view tests
    '''
    def setUp(self):
        self.board = Board.objects.create(
            name='Test', description='Test board.')
        self.username = 'test'
        self.password = '123456'
        user = User.objects.create_user(
            username=self.username, email='test@test.com',
            password=self.password)
        self.topic = Topic.objects.create(
            subject='This topic', board=self.board, starter=user)
        Post.objects.create(
            message='This is a test post', topic=self.topic, created_by=user)
        self.url = reverse(
            'reply_topic', kwargs={'pk': self.board.pk, 'topic_pk':
                                   self.topic.pk})


class LoginRequiredReplyTopicTests(ReplyTopicTestCase):
    def test_redirection(self):
        """ Test user is redirected to the sites login page """
        login_url = reverse('account_login')
        response = self.client.get(self.url)
        self.assertRedirects(
            response, '{login_url}?next={url}'.format(
                login_url=login_url, url=self.url))


class ReplyTopicTests(ReplyTopicTestCase):
    def setUp(self):
        """ Login test user """
        super().setUp()
        self.client.login(username=self.username, password=self.password)
        self.response = self.client.get(self.url)

    def test_status_code(self):
        """ Test view status code """
        self.assertEquals(self.response.status_code, 200)

    def test_view_function(self):
        """ Test url resolves to correct view """
        view = resolve('/boards/1/topics/1/reply/')
        self.assertEquals(view.func, reply_topic)

    def test_csrf(self):
        """ Test if the rendered template has a csrf token:"""
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_contains_form(self):
        """ Test if the rendered template has a form """
        form = self.response.context.get('form')
        self.assertIsInstance(form, PostForm)

    def test_form_inputs(self):
        '''
        The view must contain three inputs: csrf, subject, message textarea
        '''
        self.assertContains(self.response, '<input', 3)
        self.assertContains(self.response, '<textarea', 1)
