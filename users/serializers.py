from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers

from doc_checker.models import Document
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели User.
    Создаёт пользователя,
    шифрует пароль,
    если это модератор - даёт доступ в админку и назначает разрешения
    для редактирования документов.
    """

    class Meta:
        model = User
        fields = ['email', 'password', 'is_moderator']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        if user.is_moderator:
            user.is_staff = True
            content_type = ContentType.objects.get_for_model(Document)
            permissions = Permission.objects.filter(
                codename__in=['add_document',
                              'view_document',
                              'change_document',
                              'delete_document']
            )
            user.user_permissions.set(permissions)
        user.save()
        return user
