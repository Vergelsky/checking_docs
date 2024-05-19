from django.db import models

from doc_checker.services import send_document_verification_results


class Document(models.Model):
    status_choices = {'1_new': 'Новый',
                      '2_rej': 'Отклонён',
                      '3_conf': 'Подтверждён'}

    file = models.FileField(upload_to='docs/')
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    status = models.CharField(max_length=6, choices=status_choices, default='1_new')

    def __str__(self):
        return f'({self.status}) Документ {self.file.name} от пользователя {self.user}'

    def save(self, *args, **kwargs):
        """
        Отправляем пользователю уведомление о результатах проверки,
        если только это не создание нового документа.
        """
        if self.pk:
            send_document_verification_results(self)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'
