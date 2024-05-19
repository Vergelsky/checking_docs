from django.core.mail import EmailMessage
from users.models import User
from config.settings import DEFAULT_MODERATOR_EMAIL


def send_user_docs_for_check(doc):
    """
    Отправляет письмо с документом модератору
    Если модератора нет, то отправляет письмо на адрес DEFAULT_MODERATOR_EMAIL
    """
    moderator = (getattr(User.objects.filter(is_moderator=True).first(), 'email', None)
                 or doc.user.email)
    subject = str(doc)
    message = f'Вам необходимо проверить документ: {doc}'
    with open(doc.file.path, 'rb') as file:
        sending_file = file.read()
    email_message = EmailMessage(
        subject=subject,
        body=message,
        to=[moderator],
        attachments=[(doc.file.path, sending_file)]
    )
    try:
        email_message.send(fail_silently=False)
    except Exception as e:
        print("Ошибка отправки письма:", e)
