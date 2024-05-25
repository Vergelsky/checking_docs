from django.contrib.auth.models import Permission


def get_moder_perms():
    return Permission.objects.filter(
        codename__in=['add_document',
                      'view_document',
                      'change_document',
                      'delete_document']
    )
