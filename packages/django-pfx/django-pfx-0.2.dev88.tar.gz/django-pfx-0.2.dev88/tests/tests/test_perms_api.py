import json
import logging

from django.contrib.auth.models import User
from django.test import Client, TestCase

from pfx.pfxcore.test import TestAssertMixin
from tests.models import Author

logger = logging.getLogger(__name__)


class PermsAPITest(TestAssertMixin, TestCase):

    def setUp(self):
        self.client = Client()
        response = self.client.post(
            '/api/auth/login', {
                'username': 'jrr.tolkien',
                'password': 'PASSWORD'},
            content_type='application/json')
        token = json.loads(response.content)['token']
        self.anonymous_config = dict(
            content_type='application/json')
        self.user1_config = dict(
            HTTP_AUTHORIZATION=f'Bearer {token}',
            content_type='application/json')

    @classmethod
    def setUpTestData(cls):
        cls.user1 = User.objects.create_user(
            username='jrr.tolkien',
            email="jrr.tolkien@oxford.com",
            password='PASSWORD',
            first_name='John Ronald Reuel',
            last_name='Tolkien',
        )
        cls.author1 = Author.objects.create(
            first_name='John Ronald Reuel',
            last_name='Tolkien',
            slug='jrr-tolkien'
        )
        cls.author2 = Author.objects.create(
            first_name='Philip Kindred',
            last_name='Dick',
            slug='philip-k-dick'
        )
        cls.author3 = Author.objects.create(
            first_name='Isaac',
            last_name='Asimov',
            slug='isaac-asimov'
        )

    def test_private_edit_api_no_user(self):
        response = self.client.get(
            '/api/private-edit/authors', **self.anonymous_config)
        json.loads(response.content)

        self.assertRC(response, 200)

        response = self.client.put(
            f'/api/private-edit/authors/{self.author1.pk}',
            {'first_name': 'J. R. R.'}, **self.anonymous_config)
        json.loads(response.content)

        self.assertRC(response, 401)

    def test_private_edit_api_user(self):
        response = self.client.get(
            '/api/private-edit/authors', **self.user1_config)
        json.loads(response.content)

        self.assertRC(response, 200)

        response = self.client.put(
            f'/api/private-edit/authors/{self.author1.pk}',
            {'first_name': 'J. R. R.'}, **self.user1_config)
        json.loads(response.content)

        self.assertRC(response, 200)

    def test_private_api_no_user(self):
        response = self.client.get('/api/private/authors')
        json.loads(response.content)

        self.assertRC(response, 401)

    def test_private_api_user(self):
        response = self.client.get(
            '/api/private/authors', **self.user1_config)
        json.loads(response.content)

        self.assertRC(response, 200)

    def test_perm_api_no_admin(self):
        response = self.client.get(
            '/api/admin/authors', **self.user1_config)
        json.loads(response.content)

        self.assertRC(response, 403)

    def test_perm_api_admin(self):
        self.user1.is_superuser = True
        self.user1.save()

        response = self.client.get(
            '/api/admin/authors', **self.user1_config)
        json.loads(response.content)

        self.assertRC(response, 200)

    def test_perm_edit_api_no_admin(self):
        response = self.client.get(
            '/api/admin-edit/authors', **self.user1_config)
        json.loads(response.content)

        self.assertRC(response, 200)

        response = self.client.put(
            f'/api/admin-edit/authors/{self.author1.pk}',
            {'first_name': 'J. R. R.'}, **self.user1_config)
        json.loads(response.content)

        self.assertRC(response, 403)

    def test_perm_edit_api_admin(self):
        self.user1.is_superuser = True
        self.user1.save()

        response = self.client.get(
            '/api/admin-edit/authors', **self.user1_config)
        json.loads(response.content)

        self.assertRC(response, 200)

        response = self.client.put(
            f'/api/admin-edit/authors/{self.author1.pk}',
            {'first_name': 'J. R. R.'}, **self.user1_config)
        json.loads(response.content)
        self.assertRC(response, 200)
