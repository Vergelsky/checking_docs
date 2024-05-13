from django.db import models


class Document(models.Model):
    file = models.FileField(upload_to='docs/')
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)

    def __str__(self):
        return f'Документ {self.file.name} от пользователя {self.user}'
