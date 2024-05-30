from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    is_moderator = serializers.HiddenField(default=False)
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
        user.save()
        return user
