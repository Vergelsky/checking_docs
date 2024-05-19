from django.contrib import admin

from doc_checker.models import Document
from doc_checker.services import send_document_verification_results


# Register your models here.
@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('user', 'file', 'status')
    actions = ['mark_as_confirmed', 'mark_as_rejected', 'mark_as_new']
    ordering = ('status',)

    @admin.action(description='Отметить как проверенное')
    def mark_as_confirmed(self, request, queryset):
        queryset.update(status='3_conf')

    @admin.action(description='Отметить как отклоненное')
    def mark_as_rejected(self, request, queryset):
        queryset.update(status='2_rej')

    @admin.action(description='Отметить как новое')
    def mark_as_new(self, request, queryset):
        queryset.update(status='1_new')

    # def save_formset(self, request, form, formset, change):
    #     """
    #     Если изменение было сделано через админку - отправляем уведомление о результатах
    #     проверки, если только это не создание нового документа.
    #     """
    #     send_document_verification_results()
    #     super().save_formset(request, form, formset, change)

    def save_related(request, form, formsets, change):
        """
        Если изменение было сделано через админку - отправляем уведомление о результатах
        проверки, если только это не создание нового документа.
        """
        send_document_verification_results()
        super().save_related(request, form, formsets, change)