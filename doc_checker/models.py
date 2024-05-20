from django.db import models

from doc_checker.tasks import task_send_document_verification_results


class Document(models.Model):
    status_choices = {'1_new': 'Новый',
                      '2_rej': 'Отклонён',
                      '3_conf': 'Подтверждён'}

    file = models.FileField(upload_to='docs/')
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, blank=True)
    status = models.CharField(max_length=6, choices=status_choices, default='1_new')

    def __str__(self):
        return f'({self.status}) Документ {self.file.name} от пользователя {self.user}'

    def save(self, *args, **kwargs):
        """
        Если это не новый документ,
        Если статус изменился не на 1_new,
        То отправляем результат верификации пользователю
        """
        if self.pk:
            task_send_document_verification_results.delay(self.user.email, self.status)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'
