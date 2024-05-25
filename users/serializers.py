from rest_framework import serializers

from users.models import User
from users.services import get_moder_perms


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
            permissions = get_moder_perms()
            user.user_permissions.set(permissions)
        user.save()
        return user
