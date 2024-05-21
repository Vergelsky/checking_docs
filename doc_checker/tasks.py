from celery import shared_task
from doc_checker.services import send_document_verification_results, send_user_docs_for_check


@shared_task
def task_send_document_verification_results(email, result):
    send_document_verification_results(email, result)


@shared_task
def task_send_user_docs_for_check(doc):
    send_user_docs_for_check(doc)
