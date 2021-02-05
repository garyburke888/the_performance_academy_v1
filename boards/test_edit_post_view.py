from django.forms import ModelForm
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import resolve, reverse
from .models import Board, Post, Topic
from .views import PostUpdateView


class PostUpdateViewTestCase(TestCase):
    ''' Base test case to be used in all `PostUpdateView` view tests '''
    def setUp(self):
        self.board = Board.objects.create(
            name='Test', description='Test board.')
        self.username = 'test'
        self.password = '123456'
        user = User.objects.create_user(
            username=self.username, email='test@test.com',
            password=self.password)
        self.topic = Topic.objects.create(
            subject='Test Topic', board=self.board, starter=user)
        self.post = Post.objects.create(
            message='This is a test', topic=self.topic, created_by=user)
        self.url = reverse('edit_post', kwargs={
            'pk': self.board.pk,
            'topic_pk': self.topic.pk,
            'post_pk': self.post.pk
        })


class LoginRequiredPostUpdateViewTests(PostUpdateViewTestCase):
    def test_redirection(self):
        ''' Test if only logged in users can edit the posts '''
        login_url = reverse('account_login')
        response = self.client.get(self.url)
        self.assertRedirects(
            response, '{login_url}?next={url}'.format(
                login_url=login_url, url=self.url))


class UnauthorizedPostUpdateViewTests(PostUpdateViewTestCase):
    def setUp(self):
        ''' Create a new user different from the one who posted '''
        super().setUp()
        username = 'test2'
        password = '654321'
        user = User.objects.create_user(
            username=username, email='test2@test.com', password=password)
        self.client.login(username=username, password=password)
        self.response = self.client.get(self.url)

    def test_status_code(self):
        ''' A topic should be edited only by the owner.
        Unauthorized users should get a 404 error '''
        self.assertEquals(self.response.status_code, 404)

class PostUpdateViewTests(PostUpdateViewTestCase):
    def setUp(self):
        super().setUp()
        self.client.login(username=self.username, password=self.password)
        self.response = self.client.get(self.url)

    def test_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_view_class(self):
        view = resolve('/boards/1/topics/1/posts/1/edit/')
        self.assertEquals(view.func.view_class, PostUpdateView)

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_contains_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, ModelForm)

    def test_form_inputs(self):
        '''
        The view must contain two inputs: csrf, subject, message textarea
        '''
        self.assertContains(self.response, '<input', 3)
        self.assertContains(self.response, '<textarea', 1)
