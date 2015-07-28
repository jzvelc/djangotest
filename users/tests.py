import json

from django.core.urlresolvers import reverse
from django.test import TestCase
from .models import User


class UserViewTests(TestCase):
    def test_token_login_view(self):
        user = User.objects.create_user(
            email='test@test.com',
            password='test'
        )

        response = self.client.post(reverse('api.users:login'), {
            'email': user.email,
            'password': 'test'
        })

        content = json.loads(str(response.content, encoding='utf-8'))

        self.assertEqual(response.status_code, 201)
        self.assertEqual(content['user']['id'], user.id)
