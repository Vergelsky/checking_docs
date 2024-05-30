from django.core.mail import EmailMessage, send_mail

from users.models import User
from config.settings import DEFAULT_MODERATOR_EMAIL, EMAIL_HOST_USER


def send_user_docs_for_check(doc):
    """
    Отправляет письмо с документом модератору
    Если модератора нет, то отправляет письмо на адрес DEFAULT_MODERATOR_EMAIL
    """
    doc_name = str(doc)
    doc_path = doc.file.path
    moderator = (getattr(User.objects.filter(is_moderator=True).first(), 'email', None) or DEFAULT_MODERATOR_EMAIL)
    subject = doc_name
    message = f'Вам необходимо проверить документ: {doc_name}'
    with open(doc_path, 'rb') as file:
        sending_file = file.read()
    email_message = EmailMessage(
        subject=subject,
        body=message,
        to=[moderator],
        attachments=[(doc_path, sending_file)]
    )
    try:
        email_message.send(fail_silently=False)
    except Exception as e:
        print("Ошибка отправки письма:", e)


def send_document_verification_results(email, result):
    """
    Отправляет пользователю письмо с результатами проверки документа
    """
    match result:
        case '2_rej':
            subject = 'Ваш документ был отклонен'
            message = 'Ваш документ был отклонен. Проверьте документ и попробуйте ещё раз.'
        case '3_conf':
            subject = 'Ваш документ был принят'
            message = 'Поздравляем! Ваш документ прошёл проверку и был принят.'
    try:
        print(email)
        send_mail(
            subject=subject,
            message=message,
            from_email=EMAIL_HOST_USER,
            recipient_list=[email],
            fail_silently=False
        )
    except Exception as e:
        print("Ошибка отправки письма:", e)
