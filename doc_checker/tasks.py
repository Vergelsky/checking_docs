from celery import shared_task
from doc_checker.services import send_document_verification_results


@shared_task
def task_send_document_verification_results(email, result):
    print("!!!!!!!!!!!!!")
    send_document_verification_results(email, result)
