# Create your tests here.
import datetime
import json
from datetime import date

from django.test import TestCase
from django.urls import reverse, resolve
from backend.views import *
from backend.models import User, Post, Comment

# Несколько тестов на ручки
class TestBackendUrls(TestCase):

    def test_url_login_resolves(self):
        url = '/login/'
        resolver = resolve(url)
        self.assertEqual(resolver.func, login_view)

    def test_url_signup_resolves(self):
        url = '/signup/'
        resolver = resolve(url)
        self.assertEqual(resolver.func, signup_view)


    def test_swagger_status_code(self):
        response = self.client.get(reverse('swagger-ui'))
        self.assertEqual(response.status_code, 200)

    def test_admin_status_code(self):
        response = self.client.get(reverse('admin:index'))
        self.assertEqual(response.status_code, 302)

# Несколько тестов на контроллеры
class TestBackendControllers(TestCase):
    def setUp(self):
        self.user_item = User.objects.create(name="Test", birthday=datetime.date.today())
        self.post_item = Post.objects.create(post="TestPost", user_id=self.user_item)
        self.user_item2 = User.objects.create(name="Test 2", birthday=date(2020, 1, 1))
        self.comment_item = Comment.objects.create(post="TestComment", user_id=self.user_item2, from_comment_id=self.post_item)


    def test_get_user(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test")

    def test_get_posts(self):
        response = self.client.get('/api/posts/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "TestPost")

    def test_get_comments(self):
        response = self.client.get('/api/comments/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "TestComment")

    def test_get_user_from_id(self):
        response = self.client.get(f'/api/users/{self.user_item2.id}/')
        self.assertEqual(response.status_code, 200)
        content = json.loads(response.content.decode('utf-8'))
        self.assertEqual(content.get("name"), "Test 2")
