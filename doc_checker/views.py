from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from doc_checker.models import Document
from doc_checker.permissions import IsOwner, IsModerator
from doc_checker.serializers import DocumentSerializer
from doc_checker.services import send_user_docs_for_check


class DocumentViewSet(viewsets.ModelViewSet):
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()

    #def partial_update

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        send_user_docs_for_check(serializer.instance)
        return serializer

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsAuthenticated]
        if self.action == 'retrieve':
            self.permission_classes = [IsAuthenticated, IsOwner | IsModerator]
        if self.action in ('list', 'update', 'partial_update'):
            self.permission_classes = [IsAuthenticated, IsModerator]
        return [permission() for permission in self.permission_classes]
