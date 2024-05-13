from rest_framework import viewsets

from doc_checker.models import Document
from doc_checker.serializers import DocumentSerializer


class DocumentViewSet(viewsets.ModelViewSet):
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()

    def perform_create(self, serializer):

        return serializer.save(user=self.request.user)

