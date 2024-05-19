from django.contrib import admin

from doc_checker.models import Document


# Register your models here.
@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('user', 'file', 'status')
    actions = ['mark_as_confirmed', 'mark_as_rejected', 'mark_as_new']
    ordering = ('status',)



    @admin.action(description='Отметить как проверенное')
    def mark_as_confirmed(self, request, queryset):
        queryset.update(status='c')

    @admin.action(description='Отметить как отклоненное')
    def mark_as_rejected(self, request, queryset):
        queryset.update(status='r')

    @admin.action(description='Отметить как новое')
    def mark_as_new(self, request, queryset):
        queryset.update(status='n')
