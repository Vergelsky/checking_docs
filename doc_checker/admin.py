from django.contrib import admin

from doc_checker.models import Document
from doc_checker.tasks import task_send_document_verification_results


# Register your models here.
@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('user', 'file', 'status')
    actions = ['mark_as_confirmed', 'mark_as_rejected', 'mark_as_new']
    ordering = ('status',)

    @admin.action(description='Отметить как проверенное')
    def mark_as_confirmed(self, request, queryset):
        for doc in queryset:
            task_send_document_verification_results.delay(doc.user.email, '3_conf')
        queryset.update(status='3_conf')

    @admin.action(description='Отметить как отклоненное')
    def mark_as_rejected(self, request, queryset):
        for doc in queryset:
            task_send_document_verification_results.delay(doc.user.email, '2_rej')
        queryset.update(status='2_rej')

    @admin.action(description='Отметить как новое')
    def mark_as_new(self, request, queryset):
        queryset.update(status='1_new')
