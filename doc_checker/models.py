from django.db import models


class Document(models.Model):
    status_choices = {'n': 'new',
                      'c': 'confirmed',
                      'r': 'rejected'}

    file = models.FileField(upload_to='docs/')
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=status_choices, default='n')

    def __str__(self):
        return f'({self.status}) Документ {self.file.name} от пользователя {self.user}'

