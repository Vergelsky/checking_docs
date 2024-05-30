from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import User
from users.services import get_moder_perms


class UserTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            email="test@test.tst",
            password="testpassword"
        )
        self.user.user_permissions.set(get_moder_perms())
        self.user.is_moderator = True
        self.client.force_authenticate(user=self.user)
        self.data = {
            "email": "test1@test.tst",
            "password": "testpassword"
        }
        self.upd_data = {
            "email": "test2@test.tst"
        }

    def test_create_user(self):
        """Тестируем создание пользователя"""

        response = self.client.post(reverse("users:user-list"), data=self.data)

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_read_users(self):
        """ Тестируем чтение списка пользователей"""

        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('users:user-list'))
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_update_user(self):
        """ Тестируем обновление пользователя"""

        self.client.force_authenticate(user=self.user)
        response = self.client.patch(reverse('users:user-detail',
                                             args=[self.user.pk]), data=self.upd_data)
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_delete_user(self):
        """ Тестируем удаление пользователя """

        self.client.force_authenticate(user=self.user)
        response = self.client.delete(reverse('users:user-detail',
                                              args=[self.user.pk]))
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
