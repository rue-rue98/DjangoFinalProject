from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Board, Topic, Post


class BoardTests(TestCase):
    def setUp(self):
        self.board = Board.objects.create(name='Test Board', description='Test description')

    def test_home_view_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_view_contains_board_name(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, self.board.name)

    def test_board_topics_view_status_code(self):
        url = reverse('board_topics', kwargs={'pk': self.board.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_board_topics_view_404_for_invalid_board(self):
        url = reverse('board_topics', kwargs={'pk': 9999})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)


class NewTopicTests(TestCase):
    def setUp(self):
        self.board = Board.objects.create(name='Test Board', description='Test description')
        self.user = User.objects.create_user(username='testuser', password='pass12345')

    def test_new_topic_login_required(self):
        url = reverse('new_topic', kwargs={'pk': self.board.pk})
        response = self.client.get(url)
        login_url = f"{reverse('login')}?next={url}"
        self.assertRedirects(response, login_url)

    def test_new_topic_creates_topic_and_post(self):
        self.client.login(username='testuser', password='pass12345')
        url = reverse('new_topic', kwargs={'pk': self.board.pk})
        response = self.client.post(url, {'subject': 'Hello', 'message': 'First post'})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Topic.objects.filter(subject='Hello').exists())
        self.assertTrue(Post.objects.filter(message='First post').exists())


class ReplyAndEditTests(TestCase):
    def setUp(self):
        self.board = Board.objects.create(name='Test Board', description='Test description')
        self.user = User.objects.create_user(username='testuser', password='pass12345')
        self.other_user = User.objects.create_user(username='otheruser', password='pass12345')
        self.topic = Topic.objects.create(subject='Test Topic', board=self.board, created_by=self.user)
        self.post = Post.objects.create(message='Original message', topic=self.topic, created_by=self.user)

    def test_reply_login_required(self):
        url = reverse('reply_topic', kwargs={'pk': self.board.pk, 'topic_pk': self.topic.pk})
        response = self.client.get(url)
        login_url = f"{reverse('login')}?next={url}"
        self.assertRedirects(response, login_url)

    def test_edit_post_only_author(self):
        url = reverse(
            'edit_post',
            kwargs={'pk': self.board.pk, 'topic_pk': self.topic.pk, 'post_pk': self.post.pk},
        )
        self.client.login(username='otheruser', password='pass12345')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_edit_post_updates_message(self):
        url = reverse(
            'edit_post',
            kwargs={'pk': self.board.pk, 'topic_pk': self.topic.pk, 'post_pk': self.post.pk},
        )
        self.client.login(username='testuser', password='pass12345')
        response = self.client.post(url, {'message': 'Updated message'})
        self.assertEqual(response.status_code, 302)
        self.post.refresh_from_db()
        self.assertEqual(self.post.message, 'Updated message')