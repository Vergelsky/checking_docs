from rest_framework import serializers
from rest_framework.permissions import DjangoModelPermissions

from doc_checker.models import Document


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'
        # permissions_classes = [DjangoModelPermissions]
