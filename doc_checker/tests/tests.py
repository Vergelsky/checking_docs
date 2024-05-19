from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from doc_checker.models import Document
from users.models import User


# Create your tests here.
class DocumentTestCase(APITestCase):
    def setUp(self):
        self.file = 'doc_checker/tests/test_file.pdf'
        self.simple_user = User.objects.create(email='testuser@mail.com')
        self.moderator_user = User.objects.create(email='testmoderator@mail.com', is_moderator=True)
        self.document = Document.objects.create(
                file=self.file,
                user=self.simple_user
            )

    def test_create_document(self):
        """Тестируем создание документа"""

        self.client.force_authenticate(user=self.simple_user)

        with open(self.file, 'rb') as file:
            response = self.client.post(reverse('doc_checker:doc-check-list'),
                                        data={'file': file, 'user': self.simple_user.pk})
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_read_documents(self):
        """ Тестируем чтение списка документов """

        self.client.force_authenticate(user=self.simple_user)
        response = self.client.get(reverse('doc_checker:doc-check-list'))
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_read_document(self):
        """ Тестируем чтение одного документа """

        self.client.force_authenticate(user=self.simple_user)
        response = self.client.get(reverse('doc_checker:doc-check-list'), args=[self.document.pk])
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_update_document(self):
        """ Тестируем обновление документа модератором"""

        self.client.force_authenticate(user=self.moderator_user)
        with open(self.file, 'rb') as file:
            response = self.client.patch(reverse('doc_checker:doc-check-detail', args=[self.document.pk]),
                                         data={'file': file})
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_update_another_document(self):
        """ Тестируем обновление чужого документа """

        self.client.force_authenticate(user=self.simple_user)
        with open(self.file, 'rb') as file:
            response = self.client.patch(reverse('doc_checker:doc-check-detail', args=[self.document.pk]),
                                         data={'file': file})
        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )

    def test_delete_document(self):
        """ Тестируем удаление документа """
        self.client.force_authenticate(user=self.simple_user)
        response = self.client.delete(reverse('doc_checker:doc-check-detail', args=[self.document.pk]))
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
