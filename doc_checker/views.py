from rest_framework import viewsets

from doc_checker.models import Document
from doc_checker.serializers import DocumentSerializer
from doc_checker.tasks import task_send_user_docs_for_check


class DocumentViewSet(viewsets.ModelViewSet):
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        doc = serializer.instance
        task_send_user_docs_for_check.delay(str(doc), doc.file.path)
        return serializer
