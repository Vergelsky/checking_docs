from rest_framework import viewsets

from doc_checker.models import Document
from doc_checker.serializers import DocumentSerializer
from doc_checker.services import send_user_docs_for_check
from users.permissions import IsModerator


class DocumentViewSet(viewsets.ModelViewSet):
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()

    def get_permissions(self):
        if self.action in ('update', 'partial_update'):
            self.permission_classes = [IsModerator]
        return [permission() for permission in self.permission_classes]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        send_user_docs_for_check(serializer.instance)
        return serializer

